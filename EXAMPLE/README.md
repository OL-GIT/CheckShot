# SAMPLE_PROJECT

### A sample project to test olSeqCheck. ###

**Installation**

unzip SAMPLE_PROJECT.zip where you want.

It contains 2 directories
- LOGS : Where the global logs will be stored
- S1 : a sample sequence with several shots


**Usage :**

The shots in S1 are all different :
- P01 should not return any error
- All the others return errors
- A file named Z will return an error
- A directory called Forbiden can return an error if permissions are set to 000
