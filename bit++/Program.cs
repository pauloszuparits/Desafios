// link do desafio: https://codeforces.com/problemset/problem/282/A
using System;

namespace Testes
{
   class teste
    {
        static void Main(string[] args)
        {
            int result = 0;
            int n = Convert.ToInt32(Console.ReadLine());
            for(int i = 0; i < n; i++){
                string op = Console.ReadLine();
                if(op.Contains("x") || op.Contains("X")){
                    if(op.Contains("++")){
                        result = result + 1;
                    }
                    if(op.Contains("--")){
                        result = result - 1;
                    }
                }
            }

            System.Console.WriteLine(result);
        }
    } 
}
    