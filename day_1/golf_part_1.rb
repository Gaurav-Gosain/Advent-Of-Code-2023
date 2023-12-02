p ARGF.map { |l| l.scan(/\d/).then { |x| (x.first + x.last).to_i } }.sum
