# Pagination

![](https://s3.amazonaws.com/alx-intranet.hbtn.io/uplo…d4b330d177430c0e64d0811b034c5258b6d12b37f05a53ab8)
![](https://s3.amazonaws.com/alx-intranet.hbtn.io/uplo…e469a4678e81a4f489fb4fcb6cd6307120747173066bbce9a)
![](https://s3.amazonaws.com/alx-intranet.hbtn.io/uplo…bea6e85c52e410a5b9a97c46a858489b1448507148977aa7f)

Pagination is a technique used to divide a large set of data into smaller, 
more manageable chunks or pages. It allows for efficient retrieval 
and presentation of data, especially when dealing with large datasets.
The ```paginate``` method takes two parameters: ```page_size``` and ```cursor```. page_size specifies 
the number of keys per page, and cursor is used to track the current position in the 
scan process. The method uses the SCAN command with the provided cursor and count=page_size 
to retrieve a paginated list of keys 

```
josephgreen@JosephGreen-Mugabi:~/0x00-pagination$ ./3-main.py 
AssertionError raised when out of range
Nb items: 19418
{'index': 3, 'next_index': 5, 'page_size': 2, 'data': [['2016', 'FEMALE', 'ASIAN AND PACIFIC ISLANDER', 'Emma', '99', '4'], ['2016', 'FEMALE', 'ASIAN AND PACIFIC ISLANDER', 'Emily', '99', '4']]}
{'index': 5, 'next_index': 7, 'page_size': 2, 'data': [['2016', 'FEMALE', 'ASIAN AND PACIFIC ISLANDER', 'Mia', '79', '5'], ['2016', 'FEMALE', 'ASIAN AND PACIFIC ISLANDER', 'Charlotte', '59', '6']]}
Nb items: 19417
{'index': 3, 'next_index': 6, 'page_size': 2, 'data': [['2016', 'FEMALE', 'ASIAN AND PACIFIC ISLANDER', 'Emily', '99', '4'], ['2016', 'FEMALE', 'ASIAN AND PACIFIC ISLANDER', 'Mia', '79', '5']]}
{'index': 5, 'next_index': 7, 'page_size': 2, 'data': [['2016', 'FEMALE', 'ASIAN AND PACIFIC ISLANDER', 'Mia', '79', '5'], ['2016', 'FEMALE', 'ASIAN AND PACIFIC ISLANDER', 'Charlotte', '59', '6']]}
josephgreen@JosephGreen-Mugabi:~/0x00-pagination$
```