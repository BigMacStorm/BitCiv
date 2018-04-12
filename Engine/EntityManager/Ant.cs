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
        public Guid Id { get; private set; }
        public Engine Engine;
        public Coordinates Location;
        public Coordinates OldLocation;

        private readonly int MoveRange;

        private State CurrentState;
        private readonly Random _randObj;

        private readonly Dictionary<State, Action> _functions;

        public event EventPositionUpdateHandler OnUpdatePosition;

        public Ant(Engine engine)
        {
            _randObj = new Random();
            Id = Guid.NewGuid();
            Engine = engine;
            CurrentState = State.Idle;
            var currentDirection = new Tuple<int, int>(1,1);
            MoveRange = 2;

            Location = new Coordinates(_randObj.NextDouble() * Engine.WorldSize, _randObj.NextDouble() * Engine.WorldSize);

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

            var args = new EventEntityPositionArgs(before, after);
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
            Location.ActualX += MoveRange * _randObj.NextDouble();
            Location.ActualY += MoveRange * _randObj.NextDouble();
            Location.Update();
            UpdatePosition(OldLocation, Location);
        }
    }
}
