using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Web.Http;

namespace Engine
{
	public class ValuesController : ApiController
	{
		public IEnumerable<string> Get()
		{
			return new List<string> { "test", "test2" };
		}

		// GET api/values/5 
		public int Get(int id)
		{
			System.Console.WriteLine(id);
			return id;
		}

		// POST api/values 
		public void Post([FromBody]string value)
		{
			System.Console.WriteLine(value);
		}

		// PUT api/values/5 
		public void Put(int id, [FromBody]string value)
		{
		}

		// DELETE api/values/5 
		public void Delete(int id)
		{
		}
	}
}
