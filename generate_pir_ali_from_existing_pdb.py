import os
import re
import requests

def parse_fasta(fasta_file):
    with open(fasta_file, 'r') as f:
        lines = f.readlines()
        header = lines[0].strip()
        sequence = ''.join(line.strip() for line in lines[1:] if not line.startswith('>'))
    return header, sequence

def clean_name(header):
    # Extract THIE_MYCTU from '>sp|P9WG75|THIE_MYCTU something...'
    match = re.search(r'\|([A-Z0-9]+)\|([A-Z0-9_]+)', header)
    if match:
        return match.group(2)
    else:
        return header.replace('>', '').split()[0]

def write_ali_file(seq, name, output_dir='.'):
    ali_path = os.path.join(output_dir, f"{name}.ali")
    with open(ali_path, 'w') as f:
        f.write(f">P1;{name}\n")
        f.write(f"sequence:{name}:1:A:{len(seq)}:A::::\n")  # 9 colons for Modeller
        for i in range(0, len(seq), 60):
            f.write(seq[i:i+60] + '\n')
        f.write("*\n")
    print(f"✅ {ali_path} written successfully!")

def fetch_sequences_from_pdb(pdb_id):
    """Fetch all chains and sequences from RCSB PDB for a given PDB ID."""
    sequences = {}
    entry_url = f"https://data.rcsb.org/rest/v1/core/entry/{pdb_id.lower()}"
    entry_response = requests.get(entry_url)

    if entry_response.status_code != 200:
        print(f"❌ Failed to fetch metadata for {pdb_id}")
        return sequences

    entry_data = entry_response.json()
    entity_ids = entry_data.get('rcsb_entry_container_identifiers', {}).get('polymer_entity_ids', [])

    for entity_id in entity_ids:
        entity_url = f"https://data.rcsb.org/rest/v1/core/polymer_entity/{pdb_id.lower()}/{entity_id}"
        entity_response = requests.get(entity_url)
        if entity_response.status_code != 200:
            continue

        data = entity_response.json()
        try:
            sequence = data['entity_poly']['pdbx_seq_one_letter_code_can'].replace('\n', '')
            chains = data['rcsb_polymer_entity_container_identifiers']['auth_asym_ids']
            for chain in chains:
                sequences[f"{pdb_id.upper()}_{chain}"] = {
                    'sequence': sequence,
                    'chain': chain,
                    'length': len(sequence)
                }
        except Exception as e:
            print(f"⚠️ Skipping {pdb_id} entity {entity_id}: {e}")

    return sequences

def write_pir_file(pdb_files, output_file="pdb.pir"):
    with open(output_file, 'w') as f:
        for pdb in pdb_files:
            pdb_id = os.path.splitext(os.path.basename(pdb))[0]
            chain_seq_map = fetch_sequences_from_pdb(pdb_id)

            if not chain_seq_map:
                print(f"❌ No sequences found for {pdb_id}")
                continue

            for name, data in chain_seq_map.items():
                sequence = data['sequence']
                chain = data['chain']
                length = data['length']
                f.write(f">P1;{name}\n")
                f.write(f"structureX:{pdb_id}:{1}:{chain}:{length}:{chain}::::\n")
                for i in range(0, len(sequence), 60):
                    f.write(sequence[i:i+60] + '\n')
                f.write("*\n\n")
    print(f"✅ {output_file} written with correct unique sequences for each PDB chain.")

def main():
    fasta_file = "target.fasta"
    pdb_files = [f for f in os.listdir() if f.endswith('.pdb')]

    if not os.path.exists(fasta_file):
        print("❌ target.fasta not found.")
        return

    if not pdb_files:
        print("❌ No .pdb files found in the current directory.")
        return

    header, sequence = parse_fasta(fasta_file)
    target_name = clean_name(header)
    print(f"🔍 Detected target name: {target_name}")

    write_ali_file(sequence, target_name)
    write_pir_file(pdb_files)

if __name__ == "__main__":
    main()
