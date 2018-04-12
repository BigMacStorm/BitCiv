using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Engine
{
    public class EventEntityPositionArgs : EventArgs
    {
        public EventEntityPositionArgs(Coordinates before, Coordinates now)
        {
            OldLocation = before;
            NewLocation = now;
        }

        public Coordinates OldLocation { get; }

        public Coordinates NewLocation { get; }
    }

    public delegate void EventPositionUpdateHandler(object sender, EventEntityPositionArgs args);
}
