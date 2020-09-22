using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.IO;

namespace HK.Common
{
    public class ReadDwg
    {


        public void ReadFile(string path)
        {
            if (path != ""){
                byte[] data = new byte[100];
                FileStream fs = new FileStream(path, FileMode.Append);
                StreamReader sr = new StreamReader(fs);
                //int i =  fs.Read(data,0,100);
                string s;
                for (int i = 0; i < 2; i++)
                {
                    Console.Write(sr.ReadLine());
                }
              
            }
        }
        //public Encoding GetEncoding(string filePath)
        //{
        //    FileStream fs = new FileStream(filePath, FileMode.Open, FileAccess.Read);
        //    Encoding r =Type.GetType(fs);
        //    fs.Close();
        //    return r;
        //}
       
    }
}
