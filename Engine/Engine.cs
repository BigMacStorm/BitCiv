using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Engine
{
    public class Engine
    {
        //TODO: Create config manager and inject into other managers
        //TODO: Create world manager
        //TODO: Have net manager invoke owin stuff

        private List<IEngineComponent> MgrList;
        private EntityManager EntMgr;
        private NetworkManager NetMgr;

        public float WorldSize = 100;
        public int InitialEntityCount = 2;

        public Engine()
        {
            MgrList = new List<IEngineComponent>();

            EntMgr = new EntityManager(this);
            NetMgr = new NetworkManager();
            EntMgr.Populate();
            MgrList.Add(EntMgr);
            MgrList.Add(NetMgr);

            //StateUpdate subscriptions
            EntMgr.OnStateUpdate += NetMgr.UpdateState;

            while (true)
            {
                foreach (var comp in MgrList)
                {
                    comp.Tick();
                }
            }
        }
    }
}
