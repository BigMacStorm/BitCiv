using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Engine
{
    public class Engine
    {
        private List<IEngineComponent> MgrList;
        public EntityManager EntMgr;

        public float WorldSize = 100;
        public int InitialEntityCount = 20;

        public Engine()
        {
            MgrList = new List<IEngineComponent>();

            EntMgr = new EntityManager(this);
            EntMgr.Populate();
            //MgrList.Add(EntMgr);
        }
    }
}
