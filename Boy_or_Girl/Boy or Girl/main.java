// link do desafio: https://codeforces.com/problemset/problem/236/A
import java.util.Scanner;
public class main {
	
	public static int laco(String text) {
		int cont = 0;
		String[] textSplited = text.split("");
		
		for(int i = 0; i < textSplited.length; i++) {
			for(int l = i+1; l < textSplited.length; l++) {
				if(textSplited[i].equals(textSplited[l])) {
					cont++;
					break;
				}
			}
		}
		int tam = textSplited.length-cont;
		return tam;
	}
	
	public static void main(String[] args) {
		Scanner in = new Scanner(System.in);
		String text;
		text = in.nextLine();
		
		int tam = laco(text);
		if(tam%2 == 0) {
			System.out.println("CHAT WITH HER!");
		}else {
			System.out.println("IGNORE HIM!");
		}
		
		in.close();
	}
}
