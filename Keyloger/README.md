Keylogger:
keystroke logging, often regarded as keylogging or keyboard capturing, is recording the keys struck on a keyboard,
typically covertly. Usually, the users (i.e., victims) using the keyboard are uninformed that their actions 
are being monitored. Data can then be retrieved by remote hackers that created the logging program.

Why we used java:
 1. Because we know that Java can't read anything outside of JVM (Java Virtual Machine),
  I found a practical API called jNativeHook, making it happends.
 2. Java is cross platform because a program's source code is compiled into an intermediate "bytecode" language.

Code description :

This is a Java program for a simple keylogger. A keylogger is a program that records the keys pressed on a keyboard, usually for the purpose of monitoring user activity.

The program imports various Java classes, including the java.io and java.nio.file packages for file handling, and the org.jnativehook package for registering the native hook to receive global keyboard events.

The KeyLogger class implements the NativeKeyListener interface, which defines methods to be called when a key is pressed, released, or typed. The main method registers the native hook and adds a new instance of the KeyLogger class as a listener for keyboard events.

The nativeKeyPressed method is called when a key is pressed, and writes the text representation of the key to a file called keys.txt. The nativeKeyReleased and nativeKeyTyped methods are not used in this implementation.

The try-with-resources statement is used to ensure that the output stream and writer are properly closed after writing the key to the file.


How it saves:
The keys will be written in keys.txt file and application logs will reside inside file.

Note: Don't forget to stop the key logger application after you've done logging.
