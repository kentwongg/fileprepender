File Prepender 1.0
July 6th
By Kent Wong |  kentwong@ucalgary.ca


Requirements: Java run time environment 

Can be obtained at the official oracle site
You only need the JRE (Not the JDK)
http://www.oracle.com/technetwork/java/javase/downloads/jre8-downloads-2133155.html

Then associate .JAR file types with JRE. 
a) Right click the .jar
b) open with...
c) select always open with
d) browse for app/file to open with
e) navigate to //Program Files/Java/JRE8/bin/javaw.exe
f) Ok/Open

Now JAR is associated with the JRE. This will allow you to simply drop the JAR file anywhere you need it to deploy and double click




Instructions: 

Note: This is only coded to scan for .txt files - it will not pick anything else up
It will always spit out an Output folder. If you make a mistake, ensure you delete the entire output folder and re-run it

a) Copy/Drop the JAR file into desired deployment area
b) Double click (assuming you used the instructions above to associate JAR with JRE)
c) You should see an output folder with desired contents inside

