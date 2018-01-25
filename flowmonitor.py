import httplib2
import time

class OdlUtil:
    url = ''
    def __init__(self, host, port):
        self.url = 'http://' + host + ':' + str(port)
    def install_flow(self, container_name='default',username="admin", password="admin"):
        http = httplib2.Http()
        http.add_credentials(username, password)
        headers = {'Accept': 'application/json'}
        flow_name = 'flow_' + str(int(time.time()*1000))

	    #s1组表
	    s1zubiao2='{"group": [{ "group-type": "group-select","group-id": "1","group-name": "loadbalance","buckets": {"bucket": [{"bucket-id": "1","weight": "2","action": [{"order": "0","output-action": {"output-node-connector": "4"}}]},{"bucket-id": "2","weight": "3","action": [{"order": "0","output-action": {"output-node-connector": "2"}}]},{"bucket-id": "3","weight": "2","action": [{"order": "0","output-action": {"output-node-connector": "3"}}]}]}}]}'

		s1zubiao3='{"group": [{ "group-type": "group-select","group-id": "1","group-name": "loadbalance","buckets": {"bucket": [{"bucket-id": "1","weight": "2","action": [{"order": "0","output-action": {"output-node-connector": "4"}}]},{"bucket-id": "2","weight": "2","action": [{"order": "0","output-action": {"output-node-connector": "2"}}]},{"bucket-id": "3","weight": "3","action": [{"order": "0","output-action": {"output-node-connector": "3"}}]}]}}]}'

		s1zubiao4='{"group": [{ "group-type": "group-select","group-id": "1","group-name": "loadbalance","buckets": {"bucket": [{"bucket-id": "1","weight": "3","action": [{"order": "0","output-action": {"output-node-connector": "4"}}]},{"bucket-id": "2","weight": "2","action": [{"order": "0","output-action": {"output-node-connector": "2"}}]},{"bucket-id": "3","weight": "2","action": [{"order": "0","output-action": {"output-node-connector": "3"}}]}]}}]}'
		#s1流表  使组表生效
		s1liubiao='{"flow": [{"id": "1","match": {"in-port": "1"},"instructions": {"instruction": [{"order": "0","apply-actions": {"action": [{"order": "0","group-action": {"group-id": "1"}}]}}]},"flow-name": "tmp","priority": "2000","cookie": "0x01","table_id": "0"}]}'

	    #s4组表
		s4zubiao1='{"group": [{ "group-type": "group-select","group-id": "1","group-name": "loadbalance","buckets": {"bucket": [{"bucket-id": "1","weight": "2","action": [{"order": "0","output-action": {"output-node-connector": "1"}}]},{"bucket-id": "2","weight": "2","action": [{"order": "0","output-action": {"output-node-connector": "2"}}]},{"bucket-id": "3","weight": "2","action": [{"order": "0","output-action": {"output-node-connector": "3"}}]}]}}]}'
		s4zubiao2='{"group": [{ "group-type": "group-select","group-id": "2","group-name": "loadbalance","buckets": {"bucket": [{"bucket-id": "1","weight": "2","action": [{"order": "0","output-action": {"output-node-connector": "1"}}]},{"bucket-id": "2","weight": "2","action": [{"order": "0","output-action": {"output-node-connector": "2"}}]},{"bucket-id": "3","weight": "2","action": [{"order": "0","output-action": {"output-node-connector": "3"}}]}]}}]}'
		s4zubiao3='{"group": [{ "group-type": "group-select","group-id": "3","group-name": "loadbalance","buckets": {"bucket": [{"bucket-id": "1","weight": "2","action": [{"order": "0","output-action": {"output-node-connector": "1"}}]},{"bucket-id": "2","weight": "2","action": [{"order": "0","output-action": {"output-node-connector": "2"}}]},{"bucket-id": "3","weight": "2","action": [{"order": "0","output-action": {"output-node-connector": "3"}}]}]}}]}'
	    #s4流表  使组表生效
		s4liubiao10='{"flow": [{"id": "10","match": {"in-port": "4"},"instructions": {"instruction": [{"order": "0","apply-actions": {"action": [{"order": "0","group-action": {"group-id": "1"}}]}}]},"flow-name": "tmp1","priority": "2000","cookie": "0x01","table_id": "0"}]}'
		s4liubiao11='{"flow": [{"id": "11","match": {"in-port": "5"},"instructions": {"instruction": [{"order": "0","apply-actions": {"action": [{"order": "0","group-action": {"group-id": "2"}}]}}]},"flow-name": "tmp2","priority": "2000","cookie": "0x01","table_id": "0"}]}'
		s4liubiao12='{"flow": [{"id": "12","match": {"in-port": "6"},"instructions": {"instruction": [{"order": "0","apply-actions": {"action": [{"order": "0","group-action": {"group-id": "3"}}]}}]},"flow-name": "tmp3","priority": "2000","cookie": "0x01","table_id": "0"}]}'


		s2deliubiao='{"flow": [{"id": "1","match": {"in-port": "1"},"instructions": {"instruction": [{"order": "0","apply-actions": {"action": [{"order": "0","output-action": {"output-node-connector": "2"}}]}}]},"flow-name": "s2body","priority": "1000","cookie": "0x0001","table_id": "0"}]}'
		s2deliubiao1='{"flow": [{"id": "2","match": {"in-port": "2"},"instructions": {"instruction": [{"order": "0","apply-actions": {"action": [{"order": "0","output-action": {"output-node-connector": "1"}}]}}]},"flow-name": "s2body","priority": "1000","cookie": "0x0001","table_id": "0"}]}'


		s3deliubiao='{"flow": [{"id": "1","match": {"in-port": "1"},"instructions": {"instruction": [{"order": "0","apply-actions": {"action": [{"order": "0","output-action": {"output-node-connector": "2"}}]}}]},"flow-name": "s3body","priority": "1000","cookie": "0x0001","table_id": "0"}]}'
		s3deliubiao1='{"flow": [{"id": "2","match": {"in-port": "2"},"instructions": {"instruction": [{"order": "0","apply-actions": {"action": [{"order": "0","output-action": {"output-node-connector": "1"}}]}}]},"flow-name": "s3body","priority": "1000","cookie": "0x0001","table_id": "0"}]}'

	#s4liubiao from s2 to:ip:10.0.0.2 fadao h2


		s4liubiao='{"flow": [{"id": "1","match": {"in-port": "2","ethernet-match": {"ethernet-type": {"type": "0x0800"}},"ipv4-source": "10.0.0.1/32","ipv4-destination": "10.0.0.2/32"},"instructions": {"instruction": [{"order": "0","apply-actions":{"action": [{"order": "0","output-action": {"output-node-connector": "4"}}]}}]},"flow-name": "s4froms2toh2","priority": "1000","cookie": "0x0001","table_id": "0"}]}'

	#s4liubiao from:s2 to:ip:10.0.0.3 fadao h3


		s4liubiao2='{"flow": [{"id": "2","match": {"in-port": "2","ethernet-match": {"ethernet-type": {"type": "0x0800"}},"ipv4-source": "10.0.0.1/32","ipv4-destination": "10.0.0.3/32"},"instructions": {"instruction": [{"order": "0","apply-actions":{"action": [{"order": "0","output-action": {"output-node-connector": "5"}}]}}]},"flow-name": "s4froms2toh3","priority": "1000","cookie": "0x0001","table_id": "0"}]}'

	#s4liubiao from:s2 to:ip:10.0.0.4 fadao h4

		s4liubiao3='{"flow": [{"id": "3","match": {"in-port": "2","ethernet-match": {"ethernet-type": {"type": "0x0800"}},"ipv4-source": "10.0.0.1/32","ipv4-destination": "10.0.0.4/32"},"instructions": {"instruction": [{"order": "0","apply-actions":{"action": [{"order": "0","output-action": {"output-node-connector": "6"}}]}}]},"flow-name": "s4froms2toh4","priority": "1000","cookie": "0x0001","table_id": "0"}]}'

	#s4liubiao from:s3 to:ip:10.0.0.2 fadao h2

		s4liubiao4='{"flow": [{"id": "4","match": {"in-port": "1","ethernet-match": {"ethernet-type": {"type": "0x0800"}},"ipv4-source": "10.0.0.1/32","ipv4-destination": "10.0.0.2/32"},"instructions": {"instruction": [{"order": "0","apply-actions":{"action": [{"order": "0","output-action": {"output-node-connector": "4"}}]}}]},"flow-name": "s4froms1toh2","priority": "1000","cookie": "0x0001","table_id": "0"}]}'

	#s4liubiao from:s3 to:ip:10.0.0.3 fadao h3

		s4liubiao5='{"flow": [{"id": "5","match": {"in-port": "1","ethernet-match": {"ethernet-type": {"type": "0x0800"}},"ipv4-source": "10.0.0.1/32","ipv4-destination": "10.0.0.3/32"},"instructions": {"instruction": [{"order": "0","apply-actions":{"action": [{"order": "0","output-action": {"output-node-connector": "5"}}]}}]},"flow-name": "s4froms1toh3","priority": "1000","cookie": "0x0001","table_id": "0"}]}'

	#s4liubiao from:s3 to:ip:10.0.0.4 fadao h4

		s4liubiao6='{"flow": [{"id": "6","match": {"in-port": "1","ethernet-match": {"ethernet-type": {"type": "0x0800"}},"ipv4-source": "10.0.0.1/32","ipv4-destination": "10.0.0.4/32"},"instructions": {"instruction": [{"order": "0","apply-actions":{"action": [{"order": "0","output-action": {"output-node-connector": "6"}}]}}]},"flow-name": "s4froms1toh4","priority": "1000","cookie": "0x0001","table_id": "0"}]}'

	#s4liubiao from:s4 to:ip:10.0.0.2 fadao h2

		s4liubiao7='{"flow": [{"id": "7","match": {"in-port": "3","ethernet-match": {"ethernet-type": {"type": "0x0800"}},"ipv4-source": "10.0.0.1/32","ipv4-destination": "10.0.0.2/32"},"instructions": {"instruction": [{"order": "0","apply-actions":{"action": [{"order": "0","output-action": {"output-node-connector": "4"}}]}}]},"flow-name": "s4froms3toh2","priority": "1000","cookie": "0x0001","table_id": "0"}]}'

	#s4liubiao from:s4 to:ip:10.0.0.3 fadao h3
		s4liubiao8='{"flow": [{"id": "8","match": {"in-port": "3","ethernet-match": {"ethernet-type": {"type": "0x0800"}},"ipv4-source": "10.0.0.1/32","ipv4-destination": "10.0.0.3/32"},"instructions": {"instruction": [{"order": "0","apply-actions":{"action": [{"order": "0","output-action": {"output-node-connector": "5"}}]}}]},"flow-name": "s4froms3toh3","priority": "1000","cookie": "0x0001","table_id": "0"}]}'
	#s4liubiao from:s4 to:ip:10.0.0.4 fadao h4
		s4liubiao9='{"flow": [{"id": "9","match": {"in-port": "3","ethernet-match": {"ethernet-type": {"type": "0x0800"}},"ipv4-source": "10.0.0.1/32","ipv4-destination": "10.0.0.4/32"},"instructions": {"instruction": [{"order": "0","apply-actions":{"action": [{"order": "0","output-action": {"output-node-connector": "6"}}]}}]},"flow-name": "s4froms3toh4","priority": "1000","cookie": "0x0001","table_id": "0"}]}'


    	headers = {'Content-type': 'application/json'}
	num=0
	while num < 10 :
        	response, content = http.request(uri='http://127.0.0.1:8181/restconf/config/opendaylight-inventory:nodes/node/openflow:1/flow-node-inventory:group/1', body=s1zubiao4, method='PUT',headers=headers)
        	response, content = http.request(uri='http://127.0.0.1:8181/restconf/config/opendaylight-inventory:nodes/node/openflow:1/flow-node-inventory:table/0/flow/1', body=s1liubiao, method='PUT',headers=headers)
			response, content = http.request(uri='http://127.0.0.1:8181/restconf/config/opendaylight-inventory:nodes/node/openflow:4/flow-node-inventory:group/1', body=s4zubiao1, method='PUT',headers=headers)
        	response, content = http.request(uri='http://127.0.0.1:8181/restconf/config/opendaylight-inventory:nodes/node/openflow:4/flow-node-inventory:table/0/flow/10', body=s4liubiao10, method='PUT',headers=headers)
			response, content = http.request(uri='http://127.0.0.1:8181/restconf/config/opendaylight-inventory:nodes/node/openflow:4/flow-node-inventory:group/2', body=s4zubiao2, method='PUT',headers=headers)
        	response, content = http.request(uri='http://127.0.0.1:8181/restconf/config/opendaylight-inventory:nodes/node/openflow:4/flow-node-inventory:table/0/flow/11', body=s4liubiao11, method='PUT',headers=headers)
			response, content = http.request(uri='http://127.0.0.1:8181/restconf/config/opendaylight-inventory:nodes/node/openflow:4/flow-node-inventory:group/3', body=s4zubiao3, method='PUT',headers=headers)
        	response, content = http.request(uri='http://127.0.0.1:8181/restconf/config/opendaylight-inventory:nodes/node/openflow:4/flow-node-inventory:table/0/flow/12', body=s4liubiao12, method='PUT',headers=headers)              
        	response, content = http.request(uri='http://127.0.0.1:8181/restconf/config/opendaylight-inventory:nodes/node/openflow:2/flow-node-inventory:table/0/flow/1', body=s2deliubiao, method='PUT',headers=headers)
			response, content = http.request(uri='http://127.0.0.1:8181/restconf/config/opendaylight-inventory:nodes/node/openflow:2/flow-node-inventory:table/0/flow/2', body=s2deliubiao1, method='PUT',headers=headers)
        	response, content = http.request(uri='http://127.0.0.1:8181/restconf/config/opendaylight-inventory:nodes/node/openflow:3/flow-node-inventory:table/0/flow/1', body=s3deliubiao, method='PUT',headers=headers)
			response, content = http.request(uri='http://127.0.0.1:8181/restconf/config/opendaylight-inventory:nodes/node/openflow:3/flow-node-inventory:table/0/flow/2', body=s3deliubiao1, method='PUT',headers=headers)
        	response, content = http.request(uri='http://127.0.0.1:8181/restconf/config/opendaylight-inventory:nodes/node/openflow:4/flow-node-inventory:table/0/flow/1', body=s4liubiao, method='PUT',headers=headers)
        	response, content = http.request(uri='http://127.0.0.1:8181/restconf/config/opendaylight-inventory:nodes/node/openflow:4/flow-node-inventory:table/0/flow/2', body=s4liubiao2, method='PUT',headers=headers)
        	response, content = http.request(uri='http://127.0.0.1:8181/restconf/config/opendaylight-inventory:nodes/node/openflow:4/flow-node-inventory:table/0/flow/3', body=s4liubiao3, method='PUT',headers=headers)
        	response, content = http.request(uri='http://127.0.0.1:8181/restconf/config/opendaylight-inventory:nodes/node/openflow:4/flow-node-inventory:table/0/flow/4', body=s4liubiao4, method='PUT',headers=headers)
        	response, content = http.request(uri='http://127.0.0.1:8181/restconf/config/opendaylight-inventory:nodes/node/openflow:4/flow-node-inventory:table/0/flow/5', body=s4liubiao5, method='PUT',headers=headers)
        	response, content = http.request(uri='http://127.0.0.1:8181/restconf/config/opendaylight-inventory:nodes/node/openflow:4/flow-node-inventory:table/0/flow/6', body=s4liubiao6, method='PUT',headers=headers)
        	response, content = http.request(uri='http://127.0.0.1:8181/restconf/config/opendaylight-inventory:nodes/node/openflow:4/flow-node-inventory:table/0/flow/7', body=s4liubiao7, method='PUT',headers=headers)
        	response, content = http.request(uri='http://127.0.0.1:8181/restconf/config/opendaylight-inventory:nodes/node/openflow:4/flow-node-inventory:table/0/flow/8', body=s4liubiao8, method='PUT',headers=headers)
        	response, content = http.request(uri='http://127.0.0.1:8181/restconf/config/opendaylight-inventory:nodes/node/openflow:4/flow-node-inventory:table/0/flow/9', body=s4liubiao9, method='PUT',headers=headers)
			time.sleep(0.1)
			response, content = http.request(uri='http://127.0.0.1:8181/restconf/config/opendaylight-inventory:nodes/node/openflow:1/flow-node-inventory:group/1', body=s1zubiao2, method='PUT',headers=headers)
        	response, content = http.request(uri='http://127.0.0.1:8181/restconf/config/opendaylight-inventory:nodes/node/openflow:1/flow-node-inventory:table/0/flow/1', body=s1liubiao, method='PUT',headers=headers)
			time.sleep(0.1)
			response, content = http.request(uri='http://127.0.0.1:8181/restconf/config/opendaylight-inventory:nodes/node/openflow:1/flow-node-inventory:group/1', body=s1zubiao3, method='PUT',headers=headers)
        	response, content = http.request(uri='http://127.0.0.1:8181/restconf/config/opendaylight-inventory:nodes/node/openflow:1/flow-node-inventory:table/0/flow/1', body=s1liubiao, method='PUT',headers=headers)
			time.sleep(0.1)
			num=num + 1
odl = OdlUtil('127.0.0.1', '8181')
odl.install_flow()
