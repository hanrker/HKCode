using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using HK.Common;

namespace ConsoleApp1
{
    class Program
    {
        static void Main(string[] args)
        {
            //DBHelper db = new DBHelper();
            ReadDwg s = new ReadDwg();
            //string path = "D:/HKFiles/项目/演示项目/批量图纸/LT009-1.dwg";

            string path = "D:/HKFiles/项目/演示项目/00图纸/YB111.dwg";
            s.ReadFile(path);
            Console.ReadLine();
            
        }
    }
}
