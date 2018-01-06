Running the Twitter Steam Word Count Application

(If you are reading this, you have already cloned the appropriate repository from Github and navigated to the top level directory of the Twitter Stream Word Count application.)

1. Navigate down to the “extweetwordcount” directory by entering “cd extweetwordcount”. This is the directory of the Streamparse project.

2. At the command line, enter “sparse run.”

3. Wait while the Twitter stream is accessed. After a brief period, a stream of words processed by the topology will scroll up the command line interface.

4. Allow a few moments for the stream to run. The database is gathering new words and word counts.

5. Press “control” + “c” to stop the stream.

6. Navigate back up to the top level by entering “cd ..”

7. Enter “ls -l” and verify you are in the correct directory. You should see the files “finalresults.py” and “histogram.py.”

8. Get an alphabetized list of all the words streamed by entering “python finalresults.py” in the command line.

9. Get the total counts of a word of your choosing by entering “python finalresults.py [word of your choosing]”.

10. Get the words with counts between numbers of your choosing by entering “python histogram.py [x1],[x2]” where [x1] is a lower bound integer and [x2] is an upper bound integer. 

The longer the process is allowed to run in step 8, the more words will result.
