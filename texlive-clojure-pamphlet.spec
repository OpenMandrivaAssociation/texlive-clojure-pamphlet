%global tl_name clojure-pamphlet
%global tl_revision 79618

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.3
Release:	%{tl_revision}.1
Summary:	A simple literate programming tool based on clojures pamphlet system
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/web/clojure-pamphlet
License:	gpl3+
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/clojure-pamphlet.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/clojure-pamphlet.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/clojure-pamphlet.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Requires:	texlive(clojure-pamphlet.bin)
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The Clojure pamphlet system is a system based on the Clojure literate
system. In the Clojure's pamphlet system you have your main LaTeX file,
which can be compiled regularly. This file contains documentation and
source code (just like in other forms of literate programming). These
code snippets are wrapped in the chunk environment, hence they can be
recognized by the tangler in order to extract them. Chunks can be
included inside each other by the getchunk command (which will be
typeset accordingly). Finally, the LaTeX file will be run through the
tangler to get the desired chunk of code.

