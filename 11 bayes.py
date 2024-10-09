def covid_without_running_nose(p_covid, p_running_nose_have_covid, p_running_nose):

	# Applying Bayes' theorem to calculate P(C|R)
	p_covid_have_running_nose = (p_running_nose_have_covid * p_covid) / p_running_nose

	# Calculating the probability of having COVID-19 without a running nose
	p_covid_have_no_running_nose = 1 - p_covid_have_running_nose

	return p_covid_have_no_running_nose

p_covid = 0.07
p_running_nose_have_covid = 0.06
p_running_nose = 0.2

result = covid_without_running_nose(p_covid, p_running_nose_have_covid, p_running_nose)
print(f"Probability of having COVID-19 without a running nose: {result: .4f}")
