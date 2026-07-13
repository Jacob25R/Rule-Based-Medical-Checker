def run_symptom_checker():
    """A rule-based symptom checker that simulates basic medical triage tools. It evaluates user symptoms using
    conditional logic trees to provide a preliminary recommendation."""

    print("=====================================================")
    print("         Welcome to the Medical Symptom Checker      ")
    print("=====================================================")
    print("Please answer the following questions with a 'yes' or 'no'.\n")

    chest_pain = input("Do you have chest pain? (yes/no): ").strip().lower()
    shortness_of_breath = input("Are you experiencing shortness of breath? (yes/no): ").strip().lower()
    dizziness = input("Have you been feeling dizzy or lightheaded with recent head trauma? (yes/no): ").strip().lower()

    if chest_pain == "yes" or shortness_of_breath == "yes" or dizziness == "yes":
        print("========================================================")
        print("\n[!]         Red-Flag Emergency Condition Detected     ")
        print("========================================================")
        print("Result: Please seek immediate medical attention or call 911. Alert emergency services.")

        return

    fever = input("Have you been experiencing a fever? (yes/no): ").strip().lower()
    if fever == "yes":
        sore_throat = input("Do you have a sore throat? (yes/no): ").strip().lower()
        cough = input("Do you have a cough? (yes/no): ").strip().lower()
        body_ache = input("Do you have a body ache? (yes/no): ").strip().lower()

        if sore_throat == "yes":
            print("\nResult: Your symptoms may indicate an infection (e.g., Strep Throat).")
            print("Recommendation: Consult for a sample test to confirm the diagnosis.")
        elif cough == "yes" and body_ache == "yes":
            print("\nResult: Your symptoms may indicate a viral infection (e.g., Influenza).")
            print("Recommendation: Rest and stay hydrated, utilize fever-reducing over-the-counter medications. Continue to monitor closely.")
            print("If symptoms persist or worsen, consult a healthcare provider.")
        else:
            print("\nResult: Isolated fever, monitor for further symptoms.")
            print("Recommendation: Prioritize rest and hydration, fever-reducing over-the-counter medications. Monitor closely.")
    else:
        itchy_eyes = input("Do you have itchy or watery eyes? (yes/no): ").strip().lower()
        sneezing = input("Are you experiencing sneezing? (yes/no): ").strip().lower()
        known_allergies = input("Do you have any known allergies? (yes/no): ").strip().lower()

        if itchy_eyes == "yes" and sneezing == "yes" and known_allergies == "yes":
            print("\nResult: Your symptoms may indicate an allergic reaction.")
            print("Recommendation: Avoid known allergens and consider over-the-counter antihistamines.")
            print("Recommendation: Assess severity of allergic reaction to determine whether emergency care is needed.")
        else:
            print("\nResult: Symptoms do not clearly indicate a specific condition.")
            print("Recommendation: Monitor your condition and consult a healthcare provider if symptoms persist or worsen.")

if __name__ == "__main__":
    run_symptom_checker()
