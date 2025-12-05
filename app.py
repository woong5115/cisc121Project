import gradio as gr

# Helper function to check if a list is sorted in non-decreasing order
def is_sorted(lst):
    return all(lst[i] <= lst[i+1] for i in range(len(lst)-1))

def binary_search_fun(numbers, target):
    # Validate input list (ensure it's a comma-separated list of integers)
    try:
        nums = [int(x) for x in numbers.split(",")]
    except:
        return " Error: Please enter a list of integers separated by commas."

    # Validate that the target is an integer
    try:
        target = int(target)
    except:
        return " Error: Target must be an integer."

    # Binary search requires a sorted list → check before searching
    if not is_sorted(nums):
        return (
            "ERROR: Binary Search requires a SORTED LIST.\n\n"
            "Please enter numbers in non-decreasing (sorted) order.\n"
            "Example: 1, 3, 4, 7, 9"
        )

    # Store steps to display to the user
    steps = [f"List: {nums}\n"]

    # Initialize pointers
    left, right = 0, len(nums) - 1

    # Binary search loop
    while left <= right:
        mid = (left + right) // 2  # Middle index
        steps.append(f"Checking middle index {mid} → value {nums[mid]}")

        # If the target is found
        if nums[mid] == target:
            steps.append(f"Value {target} found at index {mid}. Checking for duplicates...")

            # Collect all duplicate indices
            indices = [mid]

            # Look left for duplicates
            i = mid - 1
            while i >= 0 and nums[i] == target:
                indices.append(i)
                i -= 1

            # Look right for duplicates
            i = mid + 1
            while i < len(nums) and nums[i] == target:
                indices.append(i)
                i += 1

            indices.sort()

            steps.append(f"🎉 Found ALL occurrences of {target} at indices: {indices}")
            return "\n".join(steps)

        # If middle value is too small → search right half
        elif nums[mid] < target:
            steps.append(f"{nums[mid]} < {target} → Searching RIGHT half")
            left = mid + 1

        # If middle value is too large → search left half
        else:
            steps.append(f"{nums[mid]} > {target} → Searching LEFT half")
            right = mid - 1

    # Target not found
    steps.append(f" {target} not found in the list.")
    return "\n".join(steps)


# Gradio UI setup
demo = gr.Interface(
    fn=binary_search_fun,  # Function to run
    inputs=[
        gr.Textbox(
            lines=1,
            label="Enter SORTED Numbers (comma-separated)",
            placeholder="Example: 1, 3, 5, 5, 7, 9"
        ),
        gr.Textbox(
            lines=1,
            label="Target Number",
            placeholder="Example: 5"
        )
    ],
    outputs=gr.Textbox(
        lines=12,
        label="Binary Search Steps"
    ),
    title="Binary Search Simulator",
    description="Enter a SORTED list and a target number to simulate binary search.\nThis version finds ALL duplicate occurrences."
)

# Run the Gradio app
if __name__ == "__main__":
    demo.launch()
