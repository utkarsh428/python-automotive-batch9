def largest_rectangle_area(heights):
# stack to store indices of histogram bars
    stack = []
    max_area = 0
    index = 0             
    n = len(heights)
# traverse all bars of given histogram
    while index < n:
        if not stack or heights[index] >= heights[stack[-1]]:
            stack.append(index)
            index += 1
        else:
            top_index = stack.pop()

            if not stack:
                width = index
            else:
                width = index - stack[-1] - 1

            area = heights[top_index] * width
            max_area = max(max_area, area)

    while stack:
        top_index = stack.pop()

        if not stack:
            width = index
        else:
            width = index - stack[-1] - 1
#calculate area and update maximum area
        area = heights[top_index] * width
        max_area = max(max_area, area)

    return max_area
print("=" * 45)
print("Histogram Largest Rectangle Area Calculator")
print("=" * 45)

n = int(input("Enter number of bars: "))

heights = []
for i in range(n):
    height = int(input(f"Enter height of bar {i + 1}: "))
    heights.append(height)

result = largest_rectangle_area(heights)
print("Largest Rectangle Area:", result)