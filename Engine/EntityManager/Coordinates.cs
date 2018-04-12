namespace Engine
{
    public struct Coordinates
    {
        public double ActualX;
        public double ActualY;
        public int RelativeX;
        public int RelativeY;

        public Coordinates(double x = -1.0, double y = -1.0)
        {
            ActualX = x;
            ActualY = y;
            RelativeX = (int)ActualX;
            RelativeY = (int)ActualY;
        }

        public void Update()
        {
            if (ActualX > 100) ActualX -= 100;
            if (ActualY > 100) ActualY -= 100;
            if (ActualX < 0) ActualX += 100;
            if (ActualY > 0) ActualY += 100;
            RelativeX = (int)ActualX;
            RelativeY = (int)ActualY;
        }
    }
}