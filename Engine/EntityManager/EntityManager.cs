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

        public EntityStateStruct State;

        public event EventHandler OnStateUpdate;

        public EntityManager(Engine engine)
        {
            Engine = engine;

            State.EntityMap = new HashSet<Guid>[(int)Engine.WorldSize,(int)Engine.WorldSize];
            for (var x = 0; x < Engine.WorldSize; x++)
                for (var y = 0; y < Engine.WorldSize; y++)
                    State.EntityMap[x, y] = new HashSet<Guid>();

            State.EntityList = new Dictionary<Guid, Ant>();
        }

        public void Populate()
        {
            for (var x = 0; x < Engine.InitialEntityCount; x++)
            {
                var temp = new Ant(Engine);
                State.EntityList.Add(temp.Id, temp);
                temp.OnUpdatePosition += UpdatePosition;
            }
        }

        private void UpdatePosition(object sender, EventEntityPositionArgs e)
        {
            if (e.OldLocation.RelativeY == -1) return;
            State.EntityMap[e.OldLocation.RelativeX, e.OldLocation.RelativeY].Remove(((Ant)sender).Id);
            State.EntityMap[e.NewLocation.RelativeX, e.NewLocation.RelativeY].Add(((Ant)sender).Id);
            OnStateUpdate?.Invoke(this, EventArgs.Empty);
        }

        public void Tick()
        {
            foreach (var ant in State.EntityList)
            {
                ant.Value.Tick();
            }
            OnStateUpdate?.Invoke(this, EventArgs.Empty);
        }
    }
}
