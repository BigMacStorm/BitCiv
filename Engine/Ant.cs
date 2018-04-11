using System;
using System.Collections.Generic;
using System.Data.Common;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Engine
{
    public struct Coordinates
    {
        public double ActualX;
        public double ActualY;
        public int RelativeX;
        public int RelativeY;

        public Coordinates(double x, double y)
        {
            ActualX = x;
            ActualY = y;
            RelativeX = (int)ActualX;
            RelativeY = (int)ActualY;
        }

        public void Update()
        {
            RelativeX = (int)ActualX;
            RelativeY = (int)ActualY;
        }
    }

    public class Ant
    {
        public Guid id { get; private set; }
        public Engine _Engine;
        public Coordinates Location;

        public Ant(Engine engine)
        {
            Random rand = new Random();
            id = Guid.NewGuid();
            _Engine = engine;

            Location = new Coordinates(rand.NextDouble() * _Engine.WorldSize, rand.NextDouble() * _Engine.WorldSize);

            //TODO: this doesnt work for some reason, this seems to be a new instance of this class.
            ((EntityManager)_Engine.EntMgr).AddToMap(this);
        }
    }
}
