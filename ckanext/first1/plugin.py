import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit


class First1Plugin(plugins.SingletonPlugin):
        '''An example theme plugin.

        '''
        # Declare that this class implements IConfigurer.
        plugins.implements(plugins.IConfigurer)

        def update_config(self, config):

                # Add this plugin's templates dir to CKAN's extra_template_paths, so
                # that CKAN will use this plugin's custom templates.
                toolkit.add_template_directory(config, 'templates')
                toolkit.add_public_directory(config, 'public')
                toolkit.add_resource('assets', 'first1')
