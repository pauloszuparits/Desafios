import java.util.ArrayList;
import java.util.Collections;
import java.util.Scanner;

public class main {

	public static void main(String[] args) {
		Scanner in = new Scanner(System.in);
		int numeroDeEntradas = in.nextInt();
		
		ArrayList<String> listaPrincipal = new ArrayList<String>();
		ArrayList<String> listaAuxiliar = new ArrayList<String>();
			
		int contador = 0;
		
		for(int i = 0; i < numeroDeEntradas; i++) {
			String nome = in.next();
			String nomeAuxiliar = nome;
			if(listaAuxiliar.contains(nome)) {
				contador = Collections.frequency(listaAuxiliar, nome);
				nomeAuxiliar = nome.concat(String.valueOf(contador));
				listaPrincipal.add(nomeAuxiliar);
			}else {
				listaPrincipal.add("OK");
			}
			listaAuxiliar.add(nome);
			
		}
		
		listaPrincipal.forEach((name)->System.out.println(name));
	}

}
