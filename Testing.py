					elif whiteEdge[0] == 1:
						#On the front side
						if self.cli.arrayOfValues[0][7] == "white":
							self.cli.rotateLayer("TCW")
							self.items.insert(0, "TCW")
							curWhitePositions = self.findWhiteEdges()
						if whiteEdge[1] == 1:
							"""https://ruwix.com/the-rubiks-cube/how-to-solve-the-rubiks-cube-beginners-method/step-1-first-layer-edges/							
							"FCW"
							"TCCW"
							"RCW"
							"TCW"	"""
							self.cli.rotateLayer("FCW")
							self.items.insert(0, "FCW")

							self.cli.rotateLayer("TCCW")
							self.items.insert(0, "TCCW")

							self.cli.rotateLayer("RCW")
							self.items.insert(0, "RCW")

							self.cli.rotateLayer("TCW")
							self.items.insert(0, "TCW")
							curWhitePositions = self.findWhiteEdges()
							#happy

						elif whiteEdge[1] == 3:
							"""L B R' F2'"""
							self.cli.rotateLayer("LCW")
							self.items.insert(0, "LCW")

							self.cli.rotateLayer("BCW")
							self.items.insert(0, "BCW")

							self.cli.rotateLayer("LCCW")
							self.items.insert(0, "LCCW")

							self.cli.rotateLayer("FCW")
							self.items.insert(0, "FCW")

							self.cli.rotateLayer("FCW")
							self.items.insert(0, "FCW")
							curWhitePositions = self.findWhiteEdges()
							#happy

						elif whiteEdge[1] == 5:
							#R' D' R F2

							self.cli.rotateLayer("RCCW")
							self.items.insert(0, "RCCW")

							self.cli.rotateLayer("BCCW")
							self.items.insert(0, "BCCW")

							self.cli.rotateLayer("RCW")
							self.items.insert(0, "RCW")

							self.cli.rotateLayer("FCW")
							self.items.insert(0, "FCW")	

							self.cli.rotateLayer("FCW")
							self.items.insert(0, "FCW")	
							curWhitePositions = self.findWhiteEdges()
							#happy

						elif whiteEdge[1] == 7:
							"""F' R' D' R F2"""
							self.cli.rotateLayer("FCCW")
							self.items.insert(0, "FCCW")

							self.cli.rotateLayer("RCCW")
							self.items.insert(0, "RCCW")

							self.cli.rotateLayer("BCCW")
							self.items.insert(0, "BCCW")

							self.cli.rotateLayer("RCW")
							self.items.insert(0, "RCW")

							self.cli.rotateLayer("FCW")
							self.items.insert(0, "FCW")

							self.cli.rotateLayer("FCW")
							self.items.insert(0, "FCW")
							curWhitePositions = self.findWhiteEdges()
