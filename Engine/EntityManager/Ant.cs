using System;
using System.Collections.Generic;
using System.Data.Common;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Engine
{
    public class Ant
    {
        public Guid id { get; private set; }
        public Engine _Engine;
        public Coordinates Location;
        public Coordinates OldLocation;

        private int MoveRange;

        private State CurrentState;
        private Random randObj;

        private Dictionary<State, Action> _functions;

        public event EventPositionUpdateHandler OnUpdatePosition;

        public Ant(Engine engine)
        {
            randObj = new Random();
            id = Guid.NewGuid();
            _Engine = engine;
            CurrentState = State.Idle;
            Tuple<int, int> CurrentDirection = new Tuple<int, int>(1,1);
            MoveRange = 2;

            Location = new Coordinates(randObj.NextDouble() * _Engine.WorldSize, randObj.NextDouble() * _Engine.WorldSize);

            UpdatePosition(OldLocation, Location);

            _functions = new Dictionary<State, Action>()
            {
                {State.Idle, Wander}
            };

            //((EntityManager)_Engine.EntMgr).AddToMap(this);
        }

        private void UpdatePosition(Coordinates before, Coordinates after)
        {
            if (OnUpdatePosition == null) return;

            EventEntityPositionArgs args = new EventEntityPositionArgs(before, after);
            OnUpdatePosition(this, args);
        }

        public void Tick()
        {
            //Todo: eventually want to have something like CurrentState = _NueralNet(this);
            _functions[CurrentState].Invoke();
        }

        public void Wander()
        {
            Move();
        }

        public void Move()
        {
            OldLocation = Location;
            Location.ActualX += MoveRange * randObj.NextDouble();
            Location.ActualY += MoveRange * randObj.NextDouble();
            Location.Update();
            UpdatePosition(OldLocation, Location);
        }
    }
}
