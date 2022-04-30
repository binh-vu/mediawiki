Start from the official mediawiki docker hub:

1. https://hub.docker.com/_/mediawiki
2. https://github.com/wikimedia/mediawiki-docker/blob/bc248a718e85005b966c4f84ccebc92bdce58c4f/1.37/apache/Dockerfile

The official mediawiki do not come with extensions that are enabled in english wikipedia. The list of enabled extensions related to parser can be found in this page:

1. https://www.mediawiki.org/wiki/Special:Version
2. https://www.mediawiki.org/wiki/Extensions_FAQ

We should download the extension from ExtensionDistributor to get the correct version. I have an error when using Git to install easy timeline.
List of extensions:

1. https://www.mediawiki.org/wiki/Special:ExtensionDistributor/timeline
2. https://www.mediawiki.org/wiki/Special:ExtensionDistributor/TemplateData

Here is a page that need EasyTimeline extension to render a graph.

1. https://en.wikipedia.org/wiki/List_of_highest_mountains_on_Earth

Wikipedia parser is Parsoid. In this [note](https://www.mediawiki.org/wiki/Parsing/Notes/Moving_Parsoid_Into_Core) that they want to bring back parsoid to the core mediawiki and replace the native parser with Parsoid so they have the same parser for both editing and rendering, they give a hint that parsing wikitext depends on the [following](https://www.mediawiki.org/wiki/Parsing/Notes/Two_Systems_Problem#Reliance_on_state_that_Parsoid_doesn't_have_direct_access_to):

1. input wikitext
2. wiki config (including installed extensions)
3. media resources (images, audio, video)
4. PHP parser hooks that expose parsing internals and implementation details (not replicable in other parsers)
5. wiki messages (ex: cite output)
6. state of the corpus and other db state (ex: red links, bad images)
7. user state (prefs, etc.)
