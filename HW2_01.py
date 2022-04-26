my_list = [12, 2.4, "str", True, None, [1, 3], (1, 5), frozenset("1,2,3,4,5"), {1:"one", 2:"two", 3:"three"}, b"sometext", set("1,2,3,4,5")]
print(dir(my_list))
for i, v in enumerate(my_list,1):
  print(f"{i}),  {v} >>>>> {type(v)}")
