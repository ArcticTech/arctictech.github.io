# Arctic Tech Github Pages
Github Pages: https://pages.github.com/
Jekyll: https://jekyllrb.com/

MacOS comes pre-installed with ruby however we need to use the version of ruby that we install with homebrew. To do this, use homebrew to install ruby-install and chruby. See this guide for more details: https://www.youtube.com/watch?v=uZD2EQbBqPg

brew install ruby-install chruby

vim ~/.zshrc

```
# Target Ruby
source /usr/local/opt/chruby/share/chruby/chruby.sh
source /usr/local/opt/chruby/share/chruby/auto.sh
chruby ruby-3.2.2
```

ruby-install ruby -- --with-openssl-dir=$(brew --prefix openssl@1.1)

ruby --version

sudo gem install bundle

sudo gem install bundler jekyll

jekyll new arctictech-site
cd arctictech-site
bundle exec jekyll serve


Install theme

Install dependencies:
bundle install
bundle exec jekyll serve

Docs: https://jekyllrb.com/docs/




