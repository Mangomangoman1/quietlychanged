import json
ST="https://www.notion.com/help/file-storage-limits-in-notion"
BL="https://www.notion.com/help/understanding-block-usage"
BLWB="https://web.archive.org/web/20261103085941/https://www.notion.com/help/understanding-block-usage"
PR="https://www.notion.com/pricing"
IM="https://www.notion.com/help/images-files-and-media"
EX="https://www.notion.com/help/export-your-content"
UP="https://www.notion.com/help/upgrade-or-downgrade-your-plan"
C1="2026-11-25-notion-notion-s-free-plan-now-has-a-512-mb-storage-cap-and-uploads-pause-when-y"
C2="2026-11-19-notion-notion-s-pricing-faq-drops-the-promise-of-unlimited-blocks-for-solo-free"
C3="2026-10-27-notion-notion-s-pricing-page-stops-saying-unlimited-file-uploads-listing-up-to"
g={
"title":"Notion Free plan limits (Nov 2026): 512 MB storage, 5,000 blocks even for solo users, and what happens when you hit them",
"desc":"Notion's Free plan now has a 512 MB workspace storage cap and a 5,000-block limit for one-person workspaces (1,000 with two or more people). What counts, how to check, what stops, and your options. Sourced from Notion's own pages.",
"dek":"Notion's Free plan is no longer unlimited for anyone. Its help center now lists 512 MB of total file storage per workspace and a 5,000-block cap for one-person workspaces, which three weeks ago had \"unlimited blocks\". Here is what each limit counts, where to check your usage, what stops when you hit it, and what you can do, quoted from Notion's own pages.",
"published":"2026-11-25","modified":"2026-11-25",
"services":["Notion"],"changes":[C1,C2,C3],
"body":[
{"h":"The short version"},
{"ul":[
"**Storage:** a Free workspace gets \"512 MB total\" of file storage, shared by everyone in it. When you reach it, \"new uploads pause at the next daily check.\" Your existing files keep working. We logged the change in [today's report](../../changes/"+C1+"/).",
"**Blocks:** a Free workspace with one person \"can add up to 5,000 blocks\"; with two or more people it's 1,000. Every paragraph, to-do and table row is a block, and deleting content does not give blocks back. On November 3, 2026, the same help page said one-person workspaces \"have access to unlimited blocks.\"",
"**Per file:** uploads on Free are still capped at 5 MB each (5 GB on paid plans).",
"**Who:** the storage page says \"If you created your Notion workspace after November 23, 2026, free plan limits may apply.\" Notion doesn't say when, or whether, older Free workspaces move to these limits. The block page gives no date at all.",
"**Your options:** check your usage now (Settings → Usage for storage, Settings → Upgrade plan for blocks), export a backup, clean up big files, or move to a paid plan, which Notion says removes block limits and turns uploads back on \"right away.\""]},
{"h":"Notion Free plan limits at a glance"},
{"table":{"headers":["Limit","Free plan","Paid plans","What happens at the limit"],"rows":[
["**Total file storage** (per workspace)","512 MB","Plus: 256 GB + 5 GB per added member; Business: 512 GB + 10 GB per added member; Enterprise: 1 TB + 20 GB per added member (help center; the pricing page says \"Custom\")","New uploads pause at the next daily check; everything already uploaded keeps working"],
["**Blocks**, one-person workspace","Up to 5,000","Included, no block limit","After a three-day grace period, you can view, edit, move, export and delete, but not add new content"],
["**Blocks**, two or more people","1,000 per workspace","Included, no block limit","Same: no new content until you upgrade"],
["**Single file size**","5 MB","5 GB","The upload fails"],
["**Page history**","7 days","Plus 30 days, Business 90 days, Enterprise custom","n/a"],
["**External guests**","10","See the pricing page","n/a"]]}},
{"p":"Sources: Notion's help articles [File storage limits in Notion]("+ST+") and [Understanding block usage]("+BL+"), and the [pricing page]("+PR+"), all checked November 25, 2026."},
{"h":"The 512 MB storage limit: what counts"},
{"p":"Notion's help article says the limit \"covers all the files in your workspace added together\" and is \"shared across everyone in it no matter how many people there are.\" It's the total of what people \"have uploaded and can still see in your workspace.\""},
{"table":{"headers":["Counts toward 512 MB","Doesn't count"],"rows":[
["Files you add to a page: \"file, image, PDF, video, and audio blocks\"","\"Your pages, blocks, and databases\""],
["Files in a database's Files & media property","\"A file you replaced with a new one\""],
["\"Pages you save with Web Clipper\"","\"Older files that only show up in a page's version history\""],
["\"Files you bring in through an import\"","\"Anything in Trash, or on pages you've deleted or archived\""],
["\"Images Notion AI makes and saves to a page\"","\"Files you share with Notion AI as context\" and behind-the-scenes files like embed preview images"]]}},
{"p":"Two useful details: \"If the same file is used twice in one workspace, it only counts once,\" and text-only pages don't use storage at all. A Notion setup made of notes, to-do lists and databases without attachments is unlikely to get near 512 MB. Screenshots, PDFs, scanned receipts, imported files and clipped web pages are what fill it."},
{"p":"One inconsistency to know about: the pricing page describes File storage as \"Total file storage space used by your workspace including blocks, files, images and videos\", while the help article lists \"Your pages, blocks, and databases\" under what doesn't count. The help article is the more detailed of the two."},
{"h":"How to check your Notion storage usage"},
{"ol":[
"Go to **Settings → Usage**. Notion says \"Your usage is listed on this page.\"",
"Or open the workspace switcher at the bottom left. A storage meter only appears there once you've used 80% or more: \"Below 80%, the meter stays hidden.\"",
"Remember the numbers lag. \"Notion adds up your storage once a day, so both spots show your usage from the most recent daily check, not from this exact second.\""]},
{"p":"Warnings come first: \"When you reach 80% of your storage, you'll see a warning banner and the storage meter, and workspace owners and admins get an email.\""},
{"h":"What happens when a Free workspace hits 512 MB"},
{"quote":"When your workspace is out of storage, only new uploads stop. Everything you've already uploaded keeps working. You can still view, edit, download, and delete your files.","cite":"Notion Help Center, File storage limits in Notion, checked November 25, 2026","url":ST},
{"ul":[
"**Owners and admins** \"can upgrade or free up space.\"",
"**Members** \"see an option to ask an admin, which sends the admins a note.\"",
"**Guests** \"see a general message about upgrading.\"",
"**Public forms:** someone filling one out will \"see an error and can still submit without the file when that question is optional.\"",
"**Imports and Web Clipper** \"list any files they skipped, so nothing disappears quietly.\""]},
{"h":"How to free up space (and why it's slow)"},
{"p":"There are only two ways back, per Notion: \"Move to a paid plan. Uploads turn back on right away.\" Or \"Delete files you don't need, then wait for the next daily check.\" Deleting is clumsy for two reasons Notion spells out: \"There's no single screen that lists your files, so to delete a file, open the page where it lives and delete it there,\" and \"Deleting files doesn't free up space right away. It takes effect at the next daily check.\""},
{"p":"Practical order of attack, based on what the help article says counts:"},
{"ol":[
"**Start with video, audio and big PDFs.** One 5 MB file is about 1% of a 512 MB workspace.",
"**Check Web Clipper and import pages.** Both count toward storage.",
"**Swap uploads for links where you can.** Notion's media help page says you can embed videos from YouTube, Vimeo and other major sources, and you can embed an image by URL instead of uploading it.",
"**Deleting the page is enough.** Files \"on pages you've deleted or archived\" and \"Anything in Trash\" don't count, so you don't need to empty the trash for storage (it's different for blocks, below).",
"**Wait a day** and check Settings → Usage again before you assume it didn't work."]},
{"h":"The 5,000-block limit, even if you work alone"},
{"quote":"Block usage limits apply to workspaces on the Free Plan. How many blocks you can add depends on how many people are in the workspace. A workspace with just one person can add up to 5,000 blocks. A workspace with two or more people can add up to 1,000 blocks. Paid plans include blocks, so these limits don't apply.","cite":"Notion Help Center, Understanding block usage, checked November 25, 2026","url":BL},
{"p":"This is the bigger change for long-time solo users. The same page, in an [Internet Archive copy from November 3, 2026]("+BLWB+"), said restrictions applied only to Free workspaces with more than one workspace owner, and: \"Workspaces with only one member have access to unlimited blocks.\" Notion's pricing FAQ dropped its solo-user exemption between our November 16 and 19 snapshots ([our coverage](../../changes/"+C2+"/)), and on November 25 the pricing table's \"Pages & blocks: Limited for 2+ members\" row became \"Block storage: Limited\". The help page now answers the question directly: \"I'm the only person in my workspace. Do block limits apply to me? Yes.\""},
{"p":"What makes 5,000 blocks tighter than it sounds:"},
{"ul":[
"**Everything is a block.** \"Every piece of content you add is counted as a new block\": each paragraph, bullet point, to-do checkbox, image and table row.",
"**It's a lifetime count.** \"We count blocks based on the amount of content created in your workspace since signing up — deleting blocks, or emptying the trash, will not reduce your block count.\" Unlike storage, cleaning up does nothing.",
"**Automations count.** \"Content added through the API and connected tools (like MCP) counts toward your block limit too, even when you don't have Notion open.\" If an integration, AI tool or sync writes into your Free workspace, it's spending your blocks.",
"**Inviting someone cuts it to 1,000.** \"If you add a second person to a one-person workspace, the limit changes from 5,000 blocks to 1,000 blocks.\" Removing people until only one remains moves it back to 5,000. Notion suggests adding collaborators \"as guests\" instead."]},
{"p":"**Check your count:** Notion says \"You can see how many blocks you’ve used by going to Settings → Upgrade plan,\" and you'll \"see a notification in your workspace’s sidebar when you’ve used a majority of your blocks.\" Check Settings → People to see how many people are in the workspace, since that decides which limit applies."},
{"p":"**At the limit:** Notion gives \"a three-day grace period.\" After that, \"You can continue to view, edit, move, export, and delete existing content,\" but you can't add new blocks. Archiving teamspaces doesn't help: \"Teamspaces are not considered blocks.\""},
{"h":"Does this apply to my existing workspace?"},
{"p":"Notion doesn't say clearly. The storage article's only date is \"If you created your Notion workspace after November 23, 2026, free plan limits may apply.\" Read literally, that's about new workspaces, and \"may\" leaves room either way. The block-usage article has no date and is written as if it applies to every Free workspace now. We haven't found an announcement or email from Notion that sets a date for older workspaces. The safe assumption: check both meters now, because the block count is cumulative since you signed up and won't go down."},
{"h":"Your options"},
{"table":{"headers":["Option","What it gets you","Notes"],"rows":[
["**Stay on Free and tidy up**","Storage back under 512 MB after the next daily check","Doesn't help with blocks: deleting never lowers the block count"],
["**Plus**, $10 per seat/month billed yearly","256 GB storage, 5 GB files, no block limit, 30-day page history","Notion's pricing page shows yearly billing by default and says yearly saves \"up to 20%\", so monthly billing costs more. Every member of a paid workspace is a paid seat"],
["**Business**, $20 per seat/month billed yearly","512 GB storage, no block limit, 90-day history, AI credits","Same billing note"],
["**Plus for students and educators**","Plus features at no cost","Pricing FAQ: \"The Plus Plan (with a 1-member limit) is free for students and educators.\""],
["**Export and move**","A copy of everything","See below; Notion warns you \"can’t instantly recreate your workspace by reuploading your exported workspace content\""]]}},
{"p":"If you upgrade and change your mind, Notion's refund policy on the pricing page: a full refund \"if you downgrade your subscription within three days of signing up for monthly billing, or within 30 days of signing up for annual billing.\" Upgrades are charged immediately; downgrades happen \"at the end of your billing cycle.\" If you subscribed in the iOS or Android app, you manage the plan through the App Store or Google Play."},
{"h":"Export a backup before you hit either limit"},
{"ol":[
"Open **Settings** in the sidebar (desktop or web; \"You can only export your entire workspace on desktop or web\").",
"Under Workspace, select **General**.",
"Select **Export all workspace content**. Notion exports pages \"as HTML, Markdown, or CSV (for databases), along with any files you've uploaded.\"",
"Watch your email. \"Exports can take up to 30 hours to process,\" and the download link \"will expire after 7 days.\""]},
{"p":"Exports only include pages you can access, so in a shared workspace each person's private pages won't be in your copy. Exporting is allowed even after you hit the block limit."},
{"h":"Timeline"},
{"ul":[
"**October 27, 2026:** Notion's pricing page stops saying \"unlimited\" file uploads on paid plans and lists \"Up to 5 GB\" per file ([our coverage](../../changes/"+C3+"/)).",
"**November 3, 2026** (Internet Archive): the block-usage help page says one-person Free workspaces \"have access to unlimited blocks\"; the 1,000-block limit applies only with more than one workspace owner.",
"**November 16–19, 2026:** the pricing FAQ drops the solo exemption: \"you’ll be able to add a limited number of blocks before you have to upgrade.\"",
"**November 23, 2026:** the date in the storage article: workspaces created after it \"may\" get the Free plan limits.",
"**November 25, 2026:** pricing page adds the File storage row (512 MB on Free) and \"Block storage: Limited\"; help center lists 5,000 blocks for one-person workspaces and says API and MCP content counts."]},
{"h":"Checklist"},
{"ol":[
"Open **Settings → Usage** and note your storage.",
"Open **Settings → Upgrade plan** and note your block count; check **Settings → People** for how many people are in the workspace.",
"If you're near 5,000 blocks (or 1,000 with others), turn off any integration or AI tool that writes into the workspace; it spends blocks you can't get back.",
"Don't invite a second person to a solo Free workspace without knowing the limit drops to 1,000; share with guests instead.",
"Run **Export all workspace content** and keep the zip.",
"For storage, delete big uploads and wait a day; for blocks, the only fixes are a paid plan (or the free student/educator Plus plan) or starting a new place for new content."]}
],
"sources":[
["Notion Help Center: File storage limits in Notion (checked November 25, 2026)",ST],
["Notion Help Center: Understanding block usage (checked November 25, 2026)",BL],
["Notion Help Center: Understanding block usage, Internet Archive copy of November 3, 2026",BLWB],
["Notion pricing page (plan table and FAQ, checked November 25, 2026)",PR],
["Notion Help Center: Images, files & media",IM],
["Notion Help Center: Export your content",EX],
["Notion Help Center: Upgrade or downgrade your plan",UP]]}
json.dump(g,open('../../guides/notion-free-plan-limits-512-mb-storage-5000-blocks.json','w'),ensure_ascii=False,indent=1)
print("ok")
