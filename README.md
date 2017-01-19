#   Day 3 of Andela Bootcamp XIV
Clone the repo using the link above
##  AndeLabs
### Binary Search
Run the tests defined on AndeLabs. Test for word_count is saved as `test_word.py`
```bash
$ cd AndeLabs/binary_search
AndeLabs/binary_search$ pytest
no test dir found testing here: /home/nate/Documents/Andela/Bootcamp/Day3/AndeLabs/binary_search
=========================  test_b_search.py  =========================
.F....
======================================================================
FAIL: test_medium_list_search (test_b_search.BinarySearchTest)
----------------------------------------------------------------------
Traceback (most recent call last)
  File "/usr/lib/python2.7/unittest/case.py", line 331, in run
    testMethod()
  File "/AndeLabs/binary_search/test_b_search.py", line 112, in test_medium_list_search
    msg='should return {count: 0, index: 19} for 40'
  File "/usr/lib/python2.7/unittest/case.py", line 515, in assertEqual
    assertion_func(first, second, msg=msg)
  File "/usr/lib/python2.7/unittest/case.py", line 508, in _baseAssertEqual
    raise self.failureException(msg)
AssertionError: should return {count: 0, index: 19} for 40

                              no stdout                               
                              no stderr                               
*******************************************************************************
Ran 6 test cases in 0.00s (0.00s CPU), 1 failures
0 modules OK (1 failed)
failures: /AndeLabs/binary_search/test_b_search [1/6]
```
I encountered this error no matter what I tried but I suspect the test had an issue that was not corrected in time
