import webbrowser
import time

i = 0;
print "Start time: " + time.ctime();
while(i < 3):
    time.sleep(10);
    print "Time for a break!"
    i = i + 1;
    # webbrowser.open("https://www.youtube.com/watch?v=hZSrzL-kb38");

print "Done";