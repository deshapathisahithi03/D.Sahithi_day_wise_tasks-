using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Oops_Concept
{
    interface Play
    {
        void play();
    }
    public class MusicPlayer : Play
    {
        public void play()
        {
            Console.WriteLine("Playing Music");
        }
    }
    public class VideoPlayer : Play
    {
        public void play()
        {
            Console.WriteLine("Playing Video");
        }
    }
}
