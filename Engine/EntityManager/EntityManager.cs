using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Xml.Serialization;

namespace Engine
{
    public class EntityManager : IEngineComponent
    {
        public Engine Engine;

        public HashSet<Guid>[,] EntityMap;
        public Dictionary<Guid, Ant> EntityList;

        public EntityManager(Engine engine)
        {
            Engine = engine;

            EntityMap = new HashSet<Guid>[(int)Engine.WorldSize,(int)Engine.WorldSize];
            for (var x = 0; x < Engine.WorldSize; x++)
                for (var y = 0; y < Engine.WorldSize; y++)
                    EntityMap[x, y] = new HashSet<Guid>();

            EntityList = new Dictionary<Guid, Ant>();
        }

        public void Populate()
        {
            for (var x = 0; x < Engine.InitialEntityCount; x++)
            {
                var temp = new Ant(Engine);
                EntityList.Add(temp.Id, temp);
                temp.OnUpdatePosition += new EventPositionUpdateHandler(UpdatePosition);
            }
        }

        private void UpdatePosition(object sender, EventEntityPositionArgs e)
        {
            if (e.OldLocation.RelativeY == -1) return;
            EntityMap[e.OldLocation.RelativeX, e.OldLocation.RelativeY].Remove(((Ant)sender).Id);
            EntityMap[e.NewLocation.RelativeX, e.NewLocation.RelativeY].Add(((Ant)sender).Id);
        }

        public void Tick()
        {
            foreach (var ant in EntityList)
            {
                ant.Value.Tick();
            }
        }
    }
}
