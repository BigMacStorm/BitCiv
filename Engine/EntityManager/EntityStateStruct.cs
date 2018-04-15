using System;
using System.Collections.Generic;

namespace Engine
{
    public struct EntityStateStruct
    {
        public HashSet<Guid>[,] EntityMap;
        public Dictionary<Guid, Ant> EntityList;
    }
}