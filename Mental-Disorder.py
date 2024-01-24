# Followed option-1
import forward_chaining
import backward_chaining
import tracemalloc
goal_variable = 'Disorder'


def main():
    tracemalloc.start()
    disorder = backward_chaining.backward_chaining(
        goal_variable)
    print(
        f"Memory used after backward chaining: '{tracemalloc.get_traced_memory()}'")
    if disorder:
        print(f"Patient has '{disorder}'")
        forward_chaining.forward_chaining(disorder)
        print(
            f"Memory used after forward chaining: '{tracemalloc.get_traced_memory()}'")
    else:
        print("No disorder diagnosed.")

    print(f"Memory used: '{tracemalloc.get_traced_memory()}'")


main()
