color_list1 = ['white', 'green', 'yellow']
color_list2 = ['red', 'white']
diff = [item for item in color_list1 if item not in color_list2]
print(color_list1, "&", color_list2)
print("difference is", diff)
