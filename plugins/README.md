Auto Registry Parser Plugins 
=====================================  

Here are the plugins that are required.

FAQ
======

1. Question: How do I know what hives are required to parse what?
   
   Answer: You can look at the plugin code and look for the line that looks like this:
   def getPlugin(reg_sys, reg_nt='', reg_soft=''). ='' means it's not required. In this example, reg_sys is the only one that's required, so you would just need to do -sys <system_hive>

2. Question: I don't know how to code. If I give you an example of what I need can you help me?

   Answer: Sure, i'll try my best.

3. Question: I know how to code better than you. Can I help?

   Answer: Sure, anytime is a great time to help. No problem at all. I welcome it. I'm not a very good coder and there are things I know can be written better, I just don't know how to write them better at the moment. There are also plugins that can be written better, but I don't have the coding skills at the moment to do it. 

4. Question: Can I write plugins and give them to you so you can upload them?

   Answer: Anytime you want. Just send it to me with some sample data/output and i'll post it online once I verify it works properly.

5. Question: Why not just use Regripper?

   Answer: I didn't really code/script before I wrote autoreg-parse. I used it as an opportunity to learn Python and get better at scripting. The more you do this the more you realize how much of an advantage you have if you can script/code. The "new generation" of #DFIR are all using Python. That gave me better examples to learn from. I also didn't like the output formatting with RegRipper. Just a personal preference more than anything. I got frustated one day and decided to write my own.