require "pl"
-- hc = require('httpclient')

-- early
function access(a)
	for idx,val in ipairs(a) do
		assert( val.endpoint, "No enpoint for " .. idx )
	end
	_G["_a"] = a
end

endpoints={}
-- better
function endpoint(data)
	idx = table.getn(endpoints) + 1
	--io.write(idx .. ":")
	--pretty.dump(data)
	assert( data[1] , "No URL for " .. idx )
	endpoints[data[1]] = data
	endpoints[data[1]][1] = nil
	return endpoints[data[1]]
end

tasks={}
function task(data)
	--pretty.dump(data)
	idx = table.getn(tasks) + 1

	assert( data[1] , "No name on task no." .. idx )
	tasks[data[1]] = data
end

function http_task(data)
	data["__schema"] = "http-client"
	task(data)
end

function aws_task(data)
	data["__schema"] = "aws"
	task(data)
end

dofile("Whiskfile")

io.write("---endpoints--\n")
pretty.dump(endpoints)
io.write("---tasks--\n")

pretty.dump(tasks)

-- hc_ = hc.new()
-- res = hc_:head('http://httpbin.org/get')

-- pretty.dump(res)
