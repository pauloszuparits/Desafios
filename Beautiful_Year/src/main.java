// link para o desafio: https://codeforces.com/problemset/problem/271/A
import java.util.Scanner;
public class main {
	public static int func(int year1) {
		int year2 = year1;
		int flag = 0;
		while (true) {
			year2++;
			flag = 0;
			String aux = String.valueOf(year2);
			String[] year2Split = aux.split("(?<=.)");
			outerloop:
			for(int i = 0; i < year2Split.length; i++) {
				for(int l = i+1; l < year2Split.length; l++) {
					if(year2Split[i].equals(year2Split[l])) {
						flag = 1;
						break outerloop;
					}
				}
			}
			
			if(flag == 0) {
				return year2;
			}
			
		}
	}
	public static void main(String[] args) {
		Scanner in = new Scanner(System.in);
		int year1 = in.nextInt();
		int year2 = func(year1);
		System.out.println(year2);	
	}
}
