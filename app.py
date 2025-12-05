import gradio as gr

def is_sorted(lst):
    return all(lst[i] <= lst[i+1] for i in range(len(lst)-1))

def binary_search_fun(numbers, target):
    # Validate input list
    try:
        nums = [int(x) for x in numbers.split(",")]
    except:
        return "❌ Error: Please enter a list of integers separated by commas."

    # Validate target
    try:
        target = int(target)
    except:
        return "❌ Error: Target must be an integer."

    # Check if list is sorted
    if not is_sorted(nums):
        return (
            "⚠️ ERROR: Binary Search requires a SORTED LIST.\n\n"
            "Please enter numbers in non-decreasing (sorted) order.\n"
            "Example: 1, 3, 4, 7, 9"
        )

    steps = [f"List: {nums}\n"]

    left, right = 0, len(nums) - 1

    while left <= right:
        mid = (left + right) // 2
        steps.append(f"Checking middle index {mid} → value {nums[mid]}")

        if nums[mid] == target:
            steps.append(f"🎉 Found {target} at index {mid}!")
            return "\n".join(steps)

        elif nums[mid] < target:
            steps.append(f"{nums[mid]} < {target} → Searching RIGHT half")
            left = mid + 1

        else:
            steps.append(f"{nums[mid]} > {target} → Searching LEFT half")
            right = mid - 1

    steps.append(f"❌ {target} not found in the list.")
    return "\n".join(steps)


# Gradio UI
demo = gr.Interface(
    fn=binary_search_fun,
    inputs=[
        gr.Textbox(
            lines=1,
            label="Enter SORTED Numbers (comma-separated)",
            placeholder="Example: 1, 3, 5, 7, 9"
        ),
        gr.Textbox(
            lines=1,
            label="Target Number",
            placeholder="Example: 7"
        )
    ],
    outputs=gr.Textbox(
        lines=10,
        label="Binary Search Steps"
    ),
    title="🔍 Binary Search Simulator",
    description="Enter a SORTED list and a target number to simulate binary search."
)

if __name__ == "__main__":
    demo.launch()
