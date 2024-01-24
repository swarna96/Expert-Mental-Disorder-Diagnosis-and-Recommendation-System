# Followed Option-1
# Creating a shell for forward chaining
import timeit
import tracemalloc
# Define global variables

derived_conclusions = []  # List to store derived conclusions
global_conclusion_variable_queue = []  # Queue to store conclusion variables

# Define the clause variable list
clause_variables = [
    "Diagnosis",
    "",
    "",
    "",
    "",
    "BipolarDisorder",
    "PregnantOrBreastFeeding",
    "",
    "",
    "",
    "BipolarDisorder",
    "PregnantOrBreastFeeding",
    "PreviouslyUsedTreatment",
    "SevereDepression",
    "",
    "BipolarDisorder",
    "PregnantOrBreastFeeding",
    "PreviouslyUsedTreatment",
    "SevereDepression",
    "",
    "BipolarDisorder",
    "PregnantOrBreastFeeding",
    "PreviouslyUsedTreatment",
    "SevereDepression",
    "",
    "BipolarDisorder",
    "PregnantOrBreastFeeding",
    "PreviouslyUsedTreatment",
    "SevereDepression",
    "",
    "Schizophrenia",
    "SevereCondition",
    "",
    "",
    "",
    "Schizophrenia",
    "SevereCondition",
    "LongTermPatient",
    "TroubleUsingPills",
    "",
    "Schizophrenia",
    "SevereCondition",
    "LongTermPatient",
    "TroubleUsingPills",
    "",
    "Schizophrenia",
    "SevereCondition",
    "LongTermPatient",
    "",
    "",
    "SchizoAffectiveDisorder",
    "Bipolar",
    "",
    "",
    "",
    "SchizoAffectiveDisorder",
    "Bipolar",
    "Depression",
    "",
    "",
    "SchizoAffectiveDisorder",
    "Bipolar",
    "Depression",
    "",
    "",
    "MajorDepressiveDisorder ",
    "SuicidalThoughts",
    "",
    "",
    "",
    "MajorDepressiveDisorder",
    "SuicidalThoughts",
    "PregnantOrBreastFeeding",
    "PreviouslyUsedSSRI",
    "SevereSideEffects",
    "MajorDepressiveDisorder ",
    "SuicidalThoughts",
    "PregnantOrBreastFeeding",
    "PreviouslyUsedSSRI",
    "SevereSideEffects",
    "MajorDepressiveDisorder ",
    "SuicidalThoughts",
    "PregnantOrBreastFeeding",
    "PreviouslyUsedSSRI",
    "SevereSideEffects",
    "Psychosis",
    "SuicidalThoughts",
    "",
    "",
    "",
    "Psychosis",
    "SuicidalThoughts",
    "PregnantOrBreastFeeding",
    "Depression",
    "",
    "Psychosis",
    "SuicidalThoughts",
    "PregnantOrBreastFeeding",
    "Depression",
    "",
    "Psychosis",
    "SuicidalThoughts",
    "PregnantOrBreastFeeding",
    "Depression",
    "",
    "DissociativeIdentityDisorder",
    "Depression",
    "Anxiety",
    "",
    "",
    "DissociativeIdentityDisorder",
    "Depression",
    "Anxiety",
    "",
    "",
    "DissociativeIdentityDisorder",
    "Depression",
    "Anxiety",
    "",
    "",
    "DissociativeIdentityDisorder",
    "Depression",
    "Anxiety",
    "",
    "",
    "Dysthyma",
    "PregnantOrBreastFeeding",
    "",
    "",
    "",
    "Dysthyma",
    "PregnantOrBreastFeeding",
    "SevenYearsOrOlder",
    "",
    "",
    "Dysthyma",
    "PregnantOrBreastFeeding",
    "SevenYearsOrOlder",
    "",
    "",
    "Dysthyma",
    "PregnantOrBreastFeeding",
    "SevenYearsOrOlder",
    "",
    "",
    "GeneralizedAnxietyDisorder",
    "PregnantOrBreastFeeding",
    "",
    "",
    "",
    "GeneralizedAnxietyDisorder",
    "PregnantOrBreastFeeding",
    "AcuteAnxiety",
    "",
    "",
    "GeneralizedAnxietyDisorder",
    "PregnantOrBreastFeeding",
    "AcuteAnxiety",
    "",
    "",
    "ObsessiveCompulsiveDisorder",
    "SevereCondition",
    "SevenYearsOrOlder",
    "",
    "",
    "ObsessiveCompulsiveDisorder",
    "SevereCondition",
    "SevenYearsOrOlder",
    "",
    "",
    "ObsessiveCompulsiveDisorder",
    "SevereCondition",
    "EighteenYearsOrOlder",
    "",
    "",
    "ObsessiveCompulsiveDisorder",
    "SevereCondition",
    "EighteenYearsOrOlder",
    "",
    "",
    "PostTraumaticStressDisorder",
    "PregnantOrBreastFeeding",
    "",
    "",
    "",
    "PostTraumaticStressDisorder",
    "PregnantOrBreastFeeding",
    "AcuteAnxiety",
    "Flashback",
    "",
    "PostTraumaticStressDisorder",
    "PregnantOrBreastFeeding",
    "AcuteAnxiety",
    "Flashback",
    "",
    "PostTraumaticStressDisorder",
    "PregnantOrBreastFeeding",
    "AcuteAnxiety",
    "Flashback",
    "",
    "PostTraumaticStressDisorder",
    "PregnantOrBreastFeeding",
    "AcuteAnxiety",
    "Flashback",
    ""
]

# Define the variable list
variable_list = {
    "Diagnosis": "Did the system diagnosed a disorder?",
    "BipolarDisorder": "Does the patient have bipolar disorder?",
    "Schizophrenia": "Does the patient have schizophrenia?",
    "SchizoAffectiveDisorder": "Does the patient have schizo affective disorder?",
    "MajorDepressiveDisorder": "Does the patient have major depressive disorder?",
    "Psychosis": "Does the patient have psychosis?",
    "DissociativeIdentityDisorder": "Does the patient have dissociative identity disorder?",
    "Dysthyma": "Does the patient have dysthyma?",
    "GeneralizedAnxietyDisorder": "Does the patient have generalized anxiety disorder?",
    "ObsessiveCompulsiveDisorder": "Does the patient have obsessive compulsive disorder?",
    "PostTraumaticStressDisorder": "Does the patient have post traumatic stress disorder?",
    "NoDisorder": "Is the patient diagnosed with a disorder?",
    "PregnantOrBreastFeeding": "Is the patient currently pregnant or breastfeeding?",
    "PreviouslyUsedTreatment": "Did the patient previously used treatment for this disorder?",
    "SevereDepression": "Do the patient have severe depression?",
    "SevereCondition": "Does the patient have severe condition?",
    "LongTermPatient": "Is the patient a long-term patient of this disorder?",
    "TroubleUsingPills": "Does the patient have trouble using pills?",
    "Bipolar": "Does the patient have Bipolar characteristics?",
    "Depression": "Does the patient have depression?",
    "Anxiety": "Does the patient have anxiety?",
    "SuicidalThoughts": "Does the patient have suicidal thoughts?",
    "PreviouslyUsedSSRI": "Did the patient previously used SSRI drugs?",
    "SevenYearsOrOlder": "Is the patient 7 years or older?",
    "EighteenYearsOrOlder": "Is the patient 18 years or older?",
    "AcuteAnxiety": "Does the patient have acute anxiety? ",
    "Flashback": "Does the patient get flashback or nightmares?",
    "Treatment": "What treatment is suggested?"
}

# dictionary for facts/knowledge --> can adjust global variables
facts = {variable: None for variable in variable_list}

# To map with the input from backward chaining
disorder_list = {
    "POST TRAUMATIC STRESS DISORDER": "PostTraumaticStressDisorder",
    "DYSTHYMIA": "Dysthyma",
    "GENERALIZED ANXIETY DISORDER": "GeneralizedAnxietyDisorder",
    "BIPOLAR DISORDER": "BipolarDisorder",
    "DISSOCIATIVE IDENTITY DISORDER": "DissociativeIdentityDisorder",
    "SCHIZO-AFFECTIVE DISORDER": "SchizoAffectiveDisorder",
    "MAJOR DEPRESSIVE DISORDER": "MajorDepressiveDisorder",
    "OBSSESSIVE COMPULSIVE DISORDER": "ObsessiveCompulsiveDisorder",
    "SCHIZOPHRENIA": "Schizophrenia",
    "PSYCHOSIS": "Psychosis",
    "NO DISORDER": "NoDisorder"
}


class Rule:
    def __init__(self, conditions, actions):
        self.conditions = conditions
        self.actions = actions


# Define the rules with ruleNum
rules = {
    10: Rule({"NoDisorder": "Yes"},
             {"Treatment": "No treatment suggested"}),
    20: Rule({"BipolarDisorder": "Yes", "PregnantOrBreastFeeding": "Yes"}, {
        "Treatment": """therapies=[
             "Support groups",
             "Cognitive behavioral therapy",
             "Family therapy",
             "Psychotherapy"]"""}),
    30: Rule({"BipolarDisorder": "Yes", "PregnantOrBreastFeeding": "No", "PreviouslyUsedTreatment": "Yes", "SevereDepression": "Yes"}, {
        "Treatment": """therapies=[
             "Support groups",
             "Cognitive behavioral therapy",
             "Family therapy",
             "Psychotherapy"], medications = ["Anticonvulsant - Carbamazepine", "Antidepressant - AntiPsychotic - Symbax"]"""}),
    40: Rule({"BipolarDisorder": "Yes", "PregnantOrBreastFeeding": "No", "PreviouslyUsedTreatment": "Yes", "SevereDepression": "No"}, {
        "Treatment": """therapies=[
             "Support groups",
             "Cognitive behavioral therapy",
             "Family therapy",
             "Psychotherapy"], medications = ["Anticonvulsant - Carbamazepine", "AntiPsychotic - Risperidone"]"""}),
    50: Rule({"BipolarDisorder": "Yes", "PregnantOrBreastFeeding": "No", "PreviouslyUsedTreatment": "No", "SevereDepression": "No"}, {
        "Treatment": """therapies=[
             "Support groups",
             "Cognitive behavioral therapy",
             "Family therapy",
             "Psychotherapy"], medications = ["Anticonvulsant - Carbamazepine"]"""}),
    60: Rule({"BipolarDisorder": "Yes", "PregnantOrBreastFeeding": "No", "PreviouslyUsedTreatment": "No", "SevereDepression": "Yes"}, {
        "Treatment": """Therapies=[
             "Support groups",
             "Cognitive behavioral therapy",
             "Family therapy",
             "Psychotherapy"], Medications = ["Anticonvulsant - Carbamazepine", "SSRIs - Fluoxetine"]"""}),
    70: Rule({"Schizophrenia": "Yes", "SevereCondition": "Yes"}, {
        "Treatment": """Hospitalization, Therapies=[
             "Support groups",
             "Rehabilitation",
             "Family therapy",
             ]"""}),
    80: Rule({"Schizophrenia": "Yes", "SevereCondition": "No", "LongTermPatient": "Yes", "TroubleUsingPills": "Yes"}, {
        "Treatment": """Therapies=[
             "Support groups",
             "Rehabilitation",
             "Cognitive behavioral therapy",
             "Psychoeducation",
             "Family therapy",
             "Behaviour therapy"
             ], Medications = ["Injection - Aripiprazole"]"""}),
    90: Rule({"Schizophrenia": "Yes", "SevereCondition": "No", "LongTermPatient": "Yes", "TroubleUsingPills": "No"}, {
        "Treatment": """Therapies=[
             "Support groups",
             "Rehabilitation",
             "Cognitive behavioral therapy",
             "Psychoeducation",
             "Family therapy",
             "Behaviour therapy"
             ], Medications = ["Antipsychotic - Perphenazine"]"""}),
    100: Rule({"Schizophrenia": "Yes", "SevereCondition": "No", "LongTermPatient": "Yes"}, {
        "Treatment": """Therapies=[
             "Support groups",
             "Rehabilitation",
             "Cognitive behavioral therapy",
             "Psychoeducation",
             "Family therapy",
             "Behaviour therapy"
             ], Medications = ["Antipsychotic - Cariprazine"]"""}),
    110: Rule({"SchizoAffectiveDisorder": "Yes", "Bipolar": "Yes"}, {
        "Treatment": """Therapies=[
             "Psychotherapy",
             "Psychoeducation",
             "Family therapy"
             ], Medications = ["Antipsychotic - Risperidone", "Anticonvulsant - Carbamazepine"]"""}),
    120: Rule({"SchizoAffectiveDisorder": "Yes", "Bipolar": "No", "Depression": "Yes"}, {
        "Treatment": """Therapies=[
             "Psychotherapy",
             "Psychoeducation",
             "Family therapy"
             ], Medications = ["Antipsychotic - Risperidone", "Antidepressant - Fluoxetine"]"""}),
    130: Rule({"SchizoAffectiveDisorder": "Yes", "Bipolar": "No", "Depression": "No"}, {
        "Treatment": """Therapies=[
             "Psychotherapy",
             "Psychoeducation",
             "Family therapy"
             ], Medications = ["Antipsychotic - Risperidone"]"""}),
    140: Rule({"MajorDepressiveDisorder": "Yes", "SuicidalThoughts": "Yes"}, {
        "Treatment": """Hospitalization,Therapies=[
             "Cognitive Behavioral Therapy",
             "Behavior Therapy",
             "Psychotherapy"
             ]"""}),
    150: Rule({"MajorDepressiveDisorder": "Yes", "SuicidalThoughts": "No", "PregnantOrBreastFeeding": "No", "PreviouslyUsedSSRI": "Yes", "SevereSideEffects": "Yes"}, {
        "Treatment": """Therapies=[
             "Cognitive Behavioral Therapy",
             "Behavior Therapy",
             "Psychotherapy"
             ], Medications = ["Antidepressant - Phenelzine"], Food Restrictions = [Cheese, Pickles, Wine]"""}),
    160: Rule({"MajorDepressiveDisorder": "Yes", "SuicidalThoughts": "No", "PregnantOrBreastFeeding": "No", "PreviouslyUsedSSRI": "Yes", "SevereSideEffects": "No"}, {
        "Treatment": """Therapies=[
             "Cognitive Behavioral Therapy",
             "Behavior Therapy",
             "Psychotherapy"
             ], Medications = ["Antidepressant - Impramine"]"""}),
    170: Rule({"MajorDepressiveDisorder": "Yes", "SuicidalThoughts": "No", "PregnantOrBreastFeeding": "No", "PreviouslyUsedSSRI": "No"}, {
        "Treatment": """Therapies=[
             "Cognitive Behavioral Therapy",
             "Behavior Therapy",
             "Psychotherapy"
             ], Medications = ["SSRI - Fluoxetine"]"""}),
    180: Rule({"Psychosis": "Yes", "SuicidalThoughts": "Yes"}, {
        "Treatment": """Hospitalization, Therapies=[
             "Cognitive Behavioral Therapy",
             "Psychotherapy",
             "Family Therapy"
             ]"""}),
    190: Rule({"Psychosis": "Yes", "SuicidalThoughts": "No", "PregnantOrBreastFeeding": "No", "Depression": "No"}, {
        "Treatment": """Therapies=[
             "Cognitive Behavioral Therapy",
             "Psychotherapy",
             "Family Therapy"
             ], Medications = ["Antipsychotic - Olanzapine"]"""}),
    200: Rule({"Psychosis": "Yes", "SuicidalThoughts": "No", "PregnantOrBreastFeeding": "Yes"}, {
        "Treatment": """Therapies=[
             "Cognitive Behavioral Therapy",
             "Psychotherapy",
             "Family Therapy"
             ]"""}),
    210: Rule({"Psychosis": "Yes", "SuicidalThoughts": "No", "PregnantOrBreastFeeding": "No", "Depresssion": "Yes"}, {
        "Treatment": """Therapies=[
             "Cognitive Behavioral Therapy",
             "Psychotherapy",
             "Family Therapy"
             ], Medications = ["Antipsychotic - Olanzapine, Antidepressant - Fluoxetine"]"""}),
    220: Rule({"DissociativeIdentityDisorder": "Yes", "Depression": "Yes", "Anxiety": "Yes"}, {
        "Treatment": """Therapies=[
             "Cognitive Behavioral Therapy",
             "Psychoeducation",
             "Family Therapy"
             ], Medications = ["Antidepressant - Fluoxetine, Antianxiety - Clonazepam"]"""}),
    230: Rule({"DissociativeIdentityDisorder": "Yes", "Depression": "Yes", "Anxiety": "No"}, {
        "Treatment": """Therapies=[
             "Cognitive Behavioral Therapy",
             "Psychoeducation",
             "Family Therapy"
             ], Medications = ["Antidepressant - Fluoxetine"]"""}),
    240: Rule({"DissociativeIdentityDisorder": "Yes", "Depression": "No", "Anxiety": "No"}, {
        "Treatment": """Therapies=[
             "Cognitive Behavioral Therapy",
             "Psychoeducation",
             "Family Therapy"
             ]"""}),
    250: Rule({"DissociativeIdentityDisorder": "Yes", "Depression": "No", "Anxiety": "Yes"}, {
        "Treatment": """Therapies=[
             "Cognitive Behavioral Therapy",
             "Psychoeducation",
             "Family Therapy"
             ], Medications = ["Antianxiety - Clonazepam"]"""}),
    260: Rule({"Dysthyma": "Yes", "PregnantOrBreastFeeding": "Yes"}, {
        "Treatment": """Self-care=["Exercises"], Therapies=[
             "Psychotherapy"
             ]"""}),
    270: Rule({"Dysthyma": "Yes", "PregnantOrBreastFeeding": "No", "SevenYearsOrOlder": "Yes"}, {
        "Treatment": """Self-care=["Exercises"], Therapies=[
             "Psychotherapy"
             ], Medications = [SSRI - Fluoxetine, Antidepressant - Bupropion]"""}),
    280: Rule({"Dysthyma": "Yes", "PregnantOrBreastFeeding": "No", "SevenYearsOrOlder": "No"}, {
        "Treatment": """Therapies=[
             "Psychotherapy, Talk Therapy"
             ]"""}),
    290: Rule({"Dysthyma": "Yes", "PregnantOrBreastFeeding": "No", "SevenYearsOrOlder": "Yes"}, {
        "Treatment": """Self-care=["Exercises"], Therapies=[
             "Psychotherapy"
             ], Medications = [SSRI - Fluoxetine, Antidepressant - Bupropion]"""}),
    300: Rule({"GeneralizedAnxietyDisorder": "Yes", "PregnantOrBreastFeeding": "Yes"}, {
        "Treatment": """Self-care=["Exercises, Stress Management"], Therapies=[
             "Psychotherapy",
             "Mindfulness Therapies",
             "Cognitive Behavioral Therapies",
             ]"""}),
    310: Rule({"GeneralizedAnxietyDisorder": "Yes", "PregnantOrBreastFeeding": "No", "AcuteAnxiety": "Yes"}, {
        "Treatment": """Self-care=["Exercises, Stress Management"], Therapies=[
             "Psychotherapy",
             "Mindfulness Therapies",
             "Cognitive Behavioral Therapies",
             ], Medications = [SSRI - Fluoxetine, Antidepressant - Duloxetine, Benzodiazepine - Diazepam]"""}),
    320: Rule({"GeneralizedAnxietyDisorder": "Yes", "PregnantOrBreastFeeding": "No", "AcuteAnxiety": "No"}, {
        "Treatment": """Self-care=["Exercises, Stress Management"], Therapies=[
             "Psychotherapy",
             "Mindfulness Therapies",
             "Cognitive Behavioral Therapies",
             ], Medications = [SSRI - Fluoxetine, Antidepressant - Duloxetine]"""}),
    330: Rule({"ObsessiveCompulsiveDisorder": "Yes", "SevereCondition": "No", "SevenYearsOrOlder": "Yes"}, {
        "Treatment": """Self-care=["Exercises, Stress Management"], Therapies=[
             "Support Group",
             "Psychotherapy",
             "Aversion Therapy",
             "Rational Emotive Behavior Therapy",
             "Cognitive Behavioral Therapies"
             ], Medications = [SSRI - Fluoxetine, Antidepressant - Venlafaxine]"""}),
    340: Rule({"ObsessiveCompulsiveDisorder": "Yes", "SevereCondition": "No", "SevenYearsOrOlder": "No"}, {
        "Treatment": """Therapies=[
             "Support Group",
             "Psychotherapy",
             "Aversion Therapy",
             "Rational Emotive Behavior Therapy",
             "Cognitive Behavioral Therapies"
             ]"""}),
    350: Rule({"ObsessiveCompulsiveDisorder": "Yes", "SevereCondition": "Yes", "EighteenYearsOrOlder": "Yes"}, {
        "Treatment": """In-patient therapies=[
             "Support Group",
             "Psychotherapy",
             "Aversion Therapy",
             "Rational Emotive Behavior Therapy",
             "Cognitive Behavioral Therapies"
             ], Deep brain stimulation"""}),
    360: Rule({"ObsessiveCompulsiveDisorder": "Yes", "SevereCondition": "Yes", "EighteenYearsOrOlder": "No"}, {
        "Treatment": """In-patient therapies=[
             "Support Group",
             "Psychotherapy",
             "Aversion Therapy",no
             "Rational Emotive Behavior Therapy",
             "Cognitive Behavioral Therapies"
             ]"""}),
    370: Rule({"PostTraumaticStressDisorder": "Yes", "PregnantOrBreastFeeding": "Yes"}, {
        "Treatment": """Therapies=[
             "Cognitive Behavioral Therapies",
             "Eye Movement Desensitization Reprocessing"
             ]"""}),
    380: Rule({"PostTraumaticStressDisorder": "Yes", "PregnantOrBreastFeeding": "No", "AcuteAnxiety": "Yes", "Flashback": "Yes"}, {
        "Treatment": """Therapies=[
             "Cognitive Behavioral Therapies",
             "Eye Movement Desensitization Reprocessing",
             "Exposure Therapy"
             ], Medications = [SSRI - Fluoxetine, Antianxiety - Benzodiazepine]"""}),
    390: Rule({"PostTraumaticStressDisorder": "Yes", "PregnantOrBreastFeeding": "No", "AcuteAnxiety": "Yes", "Flashback": "No"}, {
        "Treatment": """Therapies=[
             "Cognitive Behavioral Therapies",
             "Eye Movement Desensitization Reprocessing"
             ], Medications = [SSRI - Fluoxetine, Antianxiety - Benzodiazepine]"""}),
    400: Rule({"PostTraumaticStressDisorder": "Yes", "PregnantOrBreastFeeding": "No", "AcuteAnxiety": "No", "Flashback": "Yes"}, {
        "Treatment": """Therapies=[
             "Cognitive Behavioral Therapies",
             "Eye Movement Desensitization Reprocessing",
             "Exposure Therapy"
             ], Medications = [SSRI - Fluoxetine]"""}),
    410: Rule({"PostTraumaticStressDisorder": "Yes", "PregnantOrBreastFeeding": "No", "AcuteAnxiety": "No", "Flashback": "No"}, {
        "Treatment": """Therapies=[
             "Cognitive Behavioral Therapies",
             "Eye Movement Desensitization Reprocessing"
             ], Medications = [SSRI - Fluoxetine"""}),
}


# Define functions to add facts and apply rules, and search for a clause variable
def add_fact(key, value):
    facts[key] = value


def validate_Ri(rule_num):
    rule = rules[rule_num]
    for condition in rule.conditions.keys():  # Check if all conditions are met in the facts
        if rule.conditions[condition].lower() != facts[condition].lower():
            return False
    apply_rule(rule.actions)
    print(f"Rule applied: {rule_num}")
    for condition in rule.conditions.keys():
        print(f"{condition} => {rule.conditions[condition]}")
    return True


def apply_rule(conclusion):
    derived_conclusions.append(list(conclusion.values())[0])
    global_conclusion_variable_queue.append(list(conclusion.keys())[0])

    # If all conditions are met, add the result as a new fact
    add_fact("Treatment", conclusion)


def search_cvl(variable):
    clause_numbers = []  # List to store all clause numbers
    for i, clause in enumerate(clause_variables):
        if variable.lower() == clause.lower():
            clause_numbers.append(i)
            # appends the clause nummber if variable name matches
    return clause_numbers  # Retrun None if variable not found


def update_VL(ci):
    # Implement the update_VL logic here
    for clause_number in range(ci, ci+5):
        if clause_variables[clause_number] != "":
            variable = clause_variables[clause_number]
            if facts[variable] == None:
                value = input(variable_list[variable])
                add_fact(variable, value)


def clause_to_rule(ci):
    if ci is not None:
        # Define the formula to compute the rule number
        # If the clause numbers in the clause variable list are sequenced like
        # 1,2,3,4,5, ......), the formula is:
        # Rule # = [({Quotient (Clause # / 4)} +1)]
        # If the rule numbers are sequenced like 10,20,30,40,50, ......), the formula is:
        # Rule # = [({Quotient (Clause # / 4)} +1) * 10]
        # It has been assumed that four slots have been assigned for each rule in the
        # Clause Variable list. If other than four has been assigned replace 4 by that
        # number.
        clause_number = ci + 1  # Adjust for 0-based indexing
        quotient = clause_number // 5
        rule_number = (quotient + 1) * 10

        print(f"Clause {ci} maps to Rule {rule_number}")
        # If want to see execution time of validate_Ri function uncomment the following code
        # execution_time = timeit.timeit(
        #     lambda: validate_Ri(rule_number), number=1)
        # print(f"Time required to run validate_Ri function is {execution_time}")
        if validate_Ri(rule_number):
            return True
        print(
            f"Variable '{clause_variables[ci]}' found in clause {ci}, but rule not applied")
        return False
    else:
        print("Invalid clause number")
        return False


# Add known facts to the knowlege base
def process_variable(variable):
    clause_numbers = search_cvl(variable)
    execution_time = timeit.timeit(lambda: search_cvl(variable), number=1)
    print(f"Time required to run search_cvl function is {execution_time}")
    if not clause_numbers:
        print(f"Variable '{variable}' not found in any clause.")
    else:
        for ci in clause_numbers:
            print(f"Variable '{variable}' found in clause {ci}")
            update_VL(ci)
            if clause_to_rule(ci):
                return

        print(f"Variable '{variable}' not found in any more clause.")


def forward_chaining(variable_to_process):
    # Declarations and Initializaitons

    # Processing
    while True:
        variable_to_process = disorder_list[variable_to_process]
        # Read the value of the given variable and call process variable
        add_fact(variable_to_process, "Yes")
        process_variable(variable_to_process)

        # If global variable queue is not empty, process variables
        while global_conclusion_variable_queue:
            var = global_conclusion_variable_queue.pop(0)
            process_variable(var)

        # Print all derived conclusions
        print("Derived Conclusions:")
        for conclusion in derived_conclusions:
            print(conclusion)
        if not global_conclusion_variable_queue:
            break
