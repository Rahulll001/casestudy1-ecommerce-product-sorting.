# E-commerce Product Sorting using Merge Sort

products = [
    ["Mouse", 500],
    ["Keyboard", 1200],
    ["Headphones", 2000],
    ["USB Cable", 200],
    ["Speaker", 1500]
]


def merge_sort(products):
    if len(products) <= 1:
        return products

    mid = len(products) // 2

    left = merge_sort(products[:mid])
    right = merge_sort(products[mid:])

    return merge(left, right)


def merge(left, right):
    result = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i][1] <= right[j][1]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])

    return result


print("E-commerce Product Sorting")
print("--------------------------")

print("\nProducts before sorting:")
for p in products:
    print(p[0], "- Rs.", p[1])

sorted_products = merge_sort(products)

print("\nProducts after sorting (Low to High Price):")
for p in sorted_products:
    print(p[0], "- Rs.", p[1])