

import requests
import os


# Elenco dei link dei file CSS
css_links = [
    'https://www.uebb.it/wp-content/plugins/different-menus-in-different-pages/public/css/different-menus-for-different-page-public.css?ver=2.2.2',
    'https://www.uebb.it/wp-content/plugins/th-widget-pack/header-footer/assets/css/header-footer-elementor.css?ver=2.2.5',
    "https://www.uebb.it/wp-content/plugins/formidable/css/formidableforms.css?ver=418617",
    "https://www.uebb.it/wp-content/plugins/th-widget-pack/assets/icons/icons.css?ver=2.2.5",
    "https://www.uebb.it/wp-content/plugins/th-widget-pack/css/global.css?ver=1680535226",
    "https://c0.wp.com/c/6.2/wp-includes/css/dist/block-library/style.min.css",
    "https://c0.wp.com/c/6.2/wp-includes/js/mediaelement/mediaelementplayer-legacy.min.css",
    "https://c0.wp.com/c/6.2/wp-includes/js/mediaelement/wp-mediaelement.min.css",
    "https://c0.wp.com/c/6.2/wp-includes/css/classic-themes.min.css",
    "https://www.uebb.it/wp-content/plugins/different-menus-in-different-pages/public/css/different-menus-for-different-page-public.css?ver=2.2.2",
    "https://www.uebb.it/wp-content/plugins/th-widget-pack/header-footer/assets/css/header-footer-elementor.css?ver=2.2.5",
    "https://www.uebb.it/wp-content/plugins/elementor/assets/lib/eicons/css/elementor-icons.min.css?ver=5.16.0",
    "https://www.uebb.it/wp-content/plugins/elementor/assets/css/frontend-legacy.min.css?ver=3.8.1",
    "https://www.uebb.it/wp-content/plugins/elementor/assets/css/frontend.min.css?ver=3.8.1",
    "https://www.uebb.it/wp-content/uploads/elementor/css/post-5.css?ver=1669299763",
    "https://www.uebb.it/wp-content/plugins/elementor/assets/lib/font-awesome/css/all.min.css?ver=3.8.1",
    "https://www.uebb.it/wp-content/plugins/elementor/assets/lib/font-awesome/css/v4-shims.min.css?ver=3.8.1",
    "https://www.uebb.it/wp-content/uploads/elementor/css/post-163.css?ver=1680535858",
    "https://www.uebb.it/wp-content/plugins/th-widget-pack/header-footer/inc/widgets-css/frontend.css?ver=2.2.5",
    "https://www.uebb.it/wp-content/plugins/elementor/assets/lib/font-awesome/css/font-awesome.min.css?ver=4.7.0",
    "https://www.uebb.it/wp-content/themes/stratusx/assets/css/app.css?ver=1",
    "https://www.uebb.it/wp-content/themes/stratusx-child/style.css?ver=6.2",
    "https://fonts.googleapis.com/css?family=Roboto%3A100%2C100italic%2C200%2C200italic%2C300%2C300italic%2C400%2C400italic%2C500%2C500italic%2C600%2C600italic%2C700%2C700italic%2C800%2C800italic%2C900%2C900italic%7CRoboto+Slab%3A100%2C100italic%2C200%2C200italic%2C300%2C300italic%2C400%2C400italic%2C500%2C500italic%2C600%2C600italic%2C700%2C700italic%2C800%2C800italic%2C900%2C900italic&amp;display=auto&amp;ver=6.2",
    "https://www.uebb.it/wp-content/plugins/elementor/assets/lib/font-awesome/css/fontawesome.min.css?ver=5.15.3",
    "https://www.uebb.it/wp-content/plugins/elementor/assets/lib/font-awesome/css/solid.min.css?ver=5.15.3",
    "https://www.uebb.it/wp-content/plugins/th-widget-pack/assets/icons/icons.css?ver=2.2.5",
    "https://www.uebb.it/wp-content/plugins/elementor/assets/lib/font-awesome/css/regular.min.css?ver=5.15.3",
    "https://c0.wp.com/p/jetpack/12.0/css/jetpack.css"
]


def read_css_from_url(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    else:
        return ''


# Crea una cartella
folder_name = 'css'
if not os.path.exists(folder_name):
    os.mkdir(folder_name)

# Crea un unico file CSS all'interno della cartella
combined_css_file_path = os.path.join(folder_name, 'combined.css')

# Leggi il contenuto di ogni file CSS e scrivilo nel file combinato
with open(combined_css_file_path, 'w') as combined_css_file:
    for css_link in css_links:
        css_content = read_css_from_url(css_link)
        combined_css_file.write(css_content)
        combined_css_file.write('\n')
