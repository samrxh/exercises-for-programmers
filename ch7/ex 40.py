id1 = {'first': 'John', 'last': 'Johnson', 'position': 'Manager', 'separation_date': '2016-12-31'}
id2 = {'first': 'Tou', 'last': 'Xiong', 'position': 'Software Engineer', 'separation_date': '2016-10-05'}
id3 = {'first': 'Michaela', 'last': 'Michaelson', 'position': 'District Manager', 'separation_date': '2015-12-19'}
id4 = {'first': 'Jake', 'last': 'Jacobson', 'position': 'Programmer', 'separation_date': ''}
id5 = {'first': 'Jacquelyn', 'last': 'Jackson', 'position': 'DBA', 'separation_date': ''}
id6 = {'first': 'Sally', 'last': 'Weber', 'position': 'Web Developer', 'separation_date': '2015-12-18'}

ids = [id1, id2, id3, id4, id5, id6]

string = input("String to filter by: ").lower()
filtered_position = filter(lambda employee: string in employee['position'].lower(), ids)
filtered_name = filter(lambda employee: string in employee['first'].lower() or string in employee['last'].lower(), ids)
print(list(filtered_name))
