using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Engine
{
    class NetworkManager : IEngineComponent
    {
        //this is going to host websockets/rest api endpoint.

        /*
         *
         * Here is how this is going to work:
         * Entity manager is going to have an function that handles updating entity list.
         * When that is called, it will throw an event which networkmanager is going to be subscribed to. It will pass a reference to its entity list.
         *
         * World manager will do the same thing, in that when you edit the list of items in the world, it will throw an event, telling the network manager to update its internal list.
         *
         * These will be non blocking updates against the owin(?) websocket/rest api stuff.
         *
         *
         */
        public void Tick()
        {
            
        }
    }
}
