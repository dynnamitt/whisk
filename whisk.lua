require "pl"
hc = require('httpclient')

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
	io.write(idx .. ":")
	pretty.dump(data)
	assert( data[1] , "No URL for " .. idx )
	endpoints[data[1]] = data
	endpoints[data[1]][1] = nil
end

dofile("access")

pretty.dump(endpoints)

hc_ = hc.new()
res = hc_:head('http://httpbin.org/get')

pretty.dump(res)
