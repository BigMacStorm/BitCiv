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
        public Engine _Engine;

        public HashSet<Guid>[,] EntityMap;
        public Dictionary<Guid, Ant> EntityList;

        public EntityManager(Engine engine)
        {
            _Engine = engine;

            EntityMap = new HashSet<Guid>[(int)_Engine.WorldSize,(int)_Engine.WorldSize];
            for (int x = 0; x < _Engine.WorldSize; x++)
                for (int y = 0; y < _Engine.WorldSize; y++)
                    EntityMap[x, y] = new HashSet<Guid>();

            EntityList = new Dictionary<Guid, Ant>();
        }

        public void Populate()
        {
            for (int x = 0; x < _Engine.InitialEntityCount; x++)
            {
                Ant temp = new Ant(_Engine);
                EntityList.Add(temp.id, temp);
            }
        }

        public void RemoveFromMap(Ant sent)
        {
            EntityMap[sent.Location.RelativeX, sent.Location.RelativeY].Remove(sent.id);
        }

        public void AddToMap(Ant sent)
        {
            EntityMap[sent.Location.RelativeX, sent.Location.RelativeY].Add(sent.id);
        }

        public void Tick()
        {
            
        }
    }
}
