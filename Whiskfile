-- filetype lua

endpoint{ "https://api.coindesk.com",
	  user = "per",
	  password = "olsen"	
	 }

endpoint{ "https://nrk.no",
  	user = "kjetil",
  	password = "midtlie" }


task{ "gen_list",
	file_deps = {"/var/somefile"},
	targets = {"/tmp/out.1"},
	cmds = {"cat {{file_deps}} > {{targets}}"} 
}

-- http_task{} -- nice to have to remove dep on curl 



function work_json(result,file_deps,etc)
	x = 1+1
end

function zippit(changes,statuses)
	y = 1+3
end

aws_task{
	"upload",
	file_deps = {"/tmp/out.1"},
	change = { "s3api.copy", payload = {} },
	status = { "s3api.list-objects", payload={} },
	zip = zippit,
  cmds = {"{{result}} > /tmp/debug-res.json", work_json }
}



