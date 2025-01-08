## infer the probability of having a disease D given the positive test result T
## find - P(D | T )

# given probabilities
P_D = 0.01 # pior probability of having a disease 
P_not_D = 1 - P_D  # probability of not having the disease 
P_T_given_D = 0.99 # Test is positive given disease 
P_T_given_not_D = 0.05  # Test is positive given no disease

# calculate P(T)
P_T = P_T_given_D * P_D + P_T_given_not_D * P_not_D

# calulate the P(D | T) using Bayes' Theorem
P_D_given_T = (P_T_given_D * P_D) / P_T


print(f"Probability of having a disease given a positive test: {P_D_given_T:.4f}")