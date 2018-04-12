using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Engine
{
    public class EventEntityPositionArgs : EventArgs
    {
        private Coordinates oldLocation;
        private Coordinates newLocation;

        public EventEntityPositionArgs(Coordinates before, Coordinates now)
        {
            oldLocation = before;
            newLocation = now;
        }

        public Coordinates OldLocation
        {
            get { return oldLocation; }
        }

        public Coordinates NewLocation
        {
            get { return newLocation; }
        }
    }

    public delegate void EventPositionUpdateHandler(object sender, EventEntityPositionArgs args);
}
